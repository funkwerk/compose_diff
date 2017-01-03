#!/usr/bin/env python3
import itertools
from yaml import load


class ComposeDiff:

    def __init__(self, filter=[], diff_versions=False, diff_instances=False):
        self.filter = filter
        self.diff_versions = diff_versions
        self.diff_instances = diff_instances

    def format(self, result, format='markdown'):
        columns = ['name']
        if self.diff_versions:
            columns.append('version')
        if self.diff_instances:
            columns.append('instances')
        CAPTIONS = {'name': 'Name', 'version': 'Version', 'instances': 'Instances'}
        res = []

        res.append([CAPTIONS[column] for column in columns])
        if format == 'markdown':
            res.append(['-' for _ in columns])
        for item in result:

            def escape(data):
                data = str(data)

                if format == 'markdown':
                    data = data.replace('_', '\_')
                    data = data.replace('|', '\|')
                if format == 'csv':
                    data = data.replace(';', '\;')
                return data

            res.append(list(escape(item[column]) for column in columns))

        def format_table(res):
            string = ''

            for item in res:
                if format == 'csv':
                    string += ';'.join(item)
                elif format == 'markdown':
                    string += '| {0} |'.format(' | '.join(item))
                string += '\n'
            return string
        return format_table(res)

    def diff(self, old, new):
        old, new = self.read(old), self.read(new)

        old_versions, new_versions = self.image_versions(old), self.image_versions(new)
        old_instances, new_instances = self.image_instances(old), self.image_instances(new)

        keys = set(itertools.chain(old_versions.keys(), new_versions.keys(), old_instances.keys(), new_instances.keys()))
        result = []

        for key in sorted(keys):
            if self.filter is not None:
                skip = True

                for filter in self.filter:
                    if filter in key:
                        skip = False
                if skip:
                    continue
            version = self.format_diff(
                old=old_versions[key] if key in old_versions else None,
                new=new_versions[key] if key in new_versions else None)
            instances = self.format_diff(
                old=old_instances[key] if key in old_instances else None,
                new=new_instances[key] if key in new_instances else None)

            result.append({'name': key.split('/')[-1], 'version': version, 'instances': instances})  # TODO: named tuple
        return result

    @staticmethod
    def format_diff(old, new):
        if old is not None and type(old) is list:
            old = ', '.join(sorted(set(old)))
        if new is not None and type(new) is list:
            new = ', '.join(sorted(set(new)))
        if old is None:
            if new is None:
                return ''
            return '{0} (new)'.format(new)
        elif new is None:
            return '{0} (deleted)'.format(old)
        elif old == new:
            return old
        return '{0} ({1})'.format(new, old)

    @staticmethod
    def read(path):
        with open(path, 'r') as file:
            return load(file.read())

    @staticmethod
    def image_versions(data):
        result = {}

        for name, content in ComposeDiff.services(data).items():
            if content is None:
                continue
            if 'image' not in content:
                continue
            image_name, tag = ComposeDiff.split_image(content['image'])

            if image_name not in result:
                result[image_name] = []
            result[image_name].append(tag)
        return result

    @staticmethod
    def image_instances(data):
        result = {}

        for name, content in ComposeDiff.services(data).items():
            if content is None:
                continue
            if 'image' not in content:
                continue
            image_name, _ = ComposeDiff.split_image(content['image'])

            if image_name not in result:
                result[image_name] = 0
            result[image_name] += 1
        return result

    @staticmethod
    def services(data):
        return data['services'] if 'services' in data else data

    @staticmethod
    def split_image(data):
        if ':' not in data.split('/')[-1]:
            return data, 'latest'
        splitted = data.split(':')
        return ':'.join(splitted[:-1]), splitted[-1]
