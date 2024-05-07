# https://adventofcode.com/2015/day/16
require 'benchmark'

RESULTS = {
  children: 3,
  cats: 7,
  samoyeds: 2,
  pomeranians: 3,
  akitas: 0,
  vizslas: 0,
  goldfish: 5,
  trees: 3,
  cars: 2,
  perfumes: 1
}.freeze

def perform
  Benchmark.measure do
    part1_match = false
    part2_match = false
    File.foreach('AOC_2015/16_aunt_sue/test_data.txt') do |line|
      matches = /Sue \d+: ([a-z]+: \d+), ([a-z]+: \d+), ([a-z]+: \d+)/.match(line)
      part1_count = 0
      part2_count = 0
      matches.captures.each do |match|
        key, value = match.split(': ')
        part2_count += 1 if %w[cats trees].include?(key) && (value.to_i > RESULTS[key.to_sym])
        part2_count += 1 if %w[pomeranians goldfish].include?(key) && (value.to_i < RESULTS[key.to_sym])
        if RESULTS[key.to_sym] == value.to_i
          part1_count += 1
          part2_count += 1 unless %w[cats trees pomeranians goldfish].include? key
        end
      end
      part1_match = line if part1_count == 3
      part2_match = line if part2_count == 3
    end
    return [part1_match, part2_match] if part1_match && part2_match
  end
end
result = perform
puts result
