#!/usr/bin/ruby

numbers = ARGV.select { |arg| arg.match?(/^-?\d+$/) }
              .map(&:to_i)
              .sort

numbers.each do |num|
  puts num
end