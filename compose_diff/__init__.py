#!/usr/bin/env python3
from yaml import load


class ComposeDiff:

    def __init__(self):
        pass

    def diff_images(self, old, new, filter):
        old = self.images(self.read(old))
        new = self.images(self.read(new))

        print('| {0} | {1} |'.format('Name', 'Version'))
        print('| - | - |')
        for key in sorted(set(list(old.keys()) + list(new.keys()))):
            if filter is not None:
                if filter not in key:
                    continue
            version = self.format_version(
                old=old[key] if key in old else None,
                new=new[key] if key in new else None)

            key = key.replace('_', '\_')
            version = version.replace('_', '\_')
            print('| {0} | {1} |'.format(key.split('/')[-1], version))

    @staticmethod
    def format_version(old, new):
        if old is None:
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
    def images(data):
        result = {}

        if 'services' in data:
            data = data['services']
        for name, content in data.items():
            if content is None:
                continue
            if 'image' not in content:
                continue
            image_name, tag = ComposeDiff.split_image(content['image'])
            result[image_name] = tag
        return result

    @staticmethod
    def split_image(data):
        if ':' not in data.split('/')[-1]:
            return data, 'latest'
        splitted = data.split(':')
        return ':'.join(splitted[:-1]), splitted[-1]
