# https://adventofcode.com/2015/day/5
require 'benchmark'
require 'set'
VOWELS = %w[a e i o u]
FORBIDDEN_LETTER_COMBINATIONS = {
  "a": 'b',
  "c": 'd',
  "p": 'q',
  "x": 'y'
}

def add_to_queue(added_char:, queue:)
  queue.map do |string|
    string << added_char
  end
  queue << added_char
end

def validate_two_letter_strings?(double_pair_store:, queue:)
  value = queue.find { |i| i.length == 2 }
  last_value = queue.find { |i| i.length == 3 }
  two_values_ago = queue.find { |i| i.length == 4 }
  test = double_pair_store.include?(value)
  if last_value && !two_values_ago
    # value like "aaa" needs to be excluded as a match because of the overlap.
    # The double_pair_store will have had this value added.
    test &&= last_value[0..1] != value if last_value
  elsif last_value && two_values_ago
    # When you have 4 identical characters in a row e.g. 'aaaa'
    # the test hasn't had a chance to be set to true because
    # previous value was "aaa" and would've been caught in the non-overlapping.
    # Unlike if the 2 letter pairs were separated.
    test &&= last_value[0..1] != value unless two_values_ago[0..1] == value
  end
  double_pair_store.add(value) if value
  test
end

def validate_three_letter_odds_match?(queue:)
  value = queue.find { |i| i.length == 3 }
  value[0] == value[2] if value
end

def perform
  nice_string_count_part_one = 0
  nice_string_count_part_two = 0
  Benchmark.measure do
    File.foreach('AOC_2015/05_santas_elves/test_data.txt') do |line|
      # Temp variables for part 1
      double_next_char = nil
      matching_next_char = nil
      test_double_char = false
      test_matching_string = false

      # Temp variables for part 1

      # Store a hash with count of repeated 2-letter combinations
      # If there is a match, clear the current combination so you don't get overlaps
      vowels_counter = 0
      double_pair_store = Set.new
      test_double_pair = false
      test_odds_match = false

      # We don't know the next string to match so we maintain a queue of the last 4 character sequences
      # e.g. for 'abcdef' at 'd' queue = ['abcd', 'bcd','cd','d']
      # This is a silly way of doing this, should just use the a string and get slices of the end.
      queue = []

      line.strip.each_char do |char|
        vowels_counter += 1 if VOWELS.include?(char)

        # Part 1, we know the next string we want to match
        # so we have it ready to compare against
        test_matching_string = true if matching_next_char == char
        matching_next_char = FORBIDDEN_LETTER_COMBINATIONS[char.to_sym]

        test_double_char = true if double_next_char == char
        double_next_char = char

        # Part 2:
        add_to_queue(added_char: char, queue:)
        test_double_pair = true if validate_two_letter_strings?(double_pair_store:,
                                                                queue:)
        test_odds_match = true if validate_three_letter_odds_match?(queue:)
      end
      nice_string_count_part_one += 1 if vowels_counter >= 3 && !test_matching_string && test_double_char
      nice_string_count_part_two += 1 if test_double_pair && test_odds_match
    end
    puts "Part 1 ##{nice_string_count_part_one}"
    puts "Part 2 ##{nice_string_count_part_two}"
  end
end
result = perform
puts result
