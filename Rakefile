task default: :test

task test: :audit
task :test do
  sh "PYTHONPATH=#{File.expand_path '.'}:$PYTHONPATH cucumber"
end

desc 'Publishes the PyPi'
task push: :generate
task :push do
  sh 'python3 setup.py sdist upload'
end

desc 'Checks style'
task audit: :rubocop
task :audit do
  ignores = %w(D100 D101 D102 D103 D104 E501 I201)

  FILES = FileList[%w(bin/compose_diff compose_diff/*.py setup.py)]
  sh "flake8 --ignore='#{ignores * ','}' #{FILES}"
  sh "pylint -E #{FILES}"
end

desc 'Checks ruby style'
task :rubocop do
  sh 'rubocop'
end

task :generate do
  sh 'pandoc --from=markdown --to=rst --output=README.rst README.md'
end

task :docker do
  sh 'docker build --tag=funkwerk/compose_diff  .'
end
