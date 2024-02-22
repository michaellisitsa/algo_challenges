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

def validate_two_letter_strings?(two_letter_matchers:, queue:)
  value = queue.find { |i| i.length == 2 }
  last_value = queue.find { |i| i.length == 3 }
  two_values_ago = queue.find { |i| i.length == 4 }
  test = two_letter_matchers.include?(value)
  if last_value && !two_values_ago
    # value like "aaa" needs to be excluded as a match because of the overlap.
    # The two_letter_matchers will have had this value added.
    test &&= last_value[0..1] != value if last_value
  elsif last_value && two_values_ago
    # When you have 4 identical characters in a row e.g. 'aaaa'
    # the test hasn't had a chance to be set to true because
    # previous value was "aaa" and would've been caught in the non-overlapping.
    # Unlike if the 2 letter pairs were separated.
    test &&= last_value[0..1] != value unless two_values_ago[0..1] == value
  end
  two_letter_matchers.add(value) if value
  test
end

def validate_three_letter_odds_match?(queue:)
  value = queue.find { |i| i.length == 3 }
  value[0] == value[2] if value
end

nice_string_count = 0
nice_string_count_part_two = 0
File.foreach('AOC_2015/05_santas_elves/data.txt') do |line|
  double_next_char = nil
  matching_next_char = nil

  # Store a hash with count of repeated 2-letter combinations
  # If there is a match, clear the current combination so you don't get overlaps
  two_letter_matchers = Set.new

  test_two_letter_strings = false
  test_three_letter_odds_match = false
  test_double_char = false
  test_matching_string = false
  vowels_counter = 0
  last_three_char_queue = []
  line.strip.each_char do |char|
    vowels_counter += 1 if VOWELS.include?(char)

    # Part 1, we know the next string we want to match
    # so we have it ready to compare against
    test_matching_string = true if matching_next_char == char
    matching_next_char = FORBIDDEN_LETTER_COMBINATIONS[char.to_sym]

    test_double_char = true if double_next_char == char
    double_next_char = char

    # Part 2:
    # We don't know the next string to match so we maintain a queue of the last 4 character sequences
    # ['abcd', 'bcd','cd','d']
    # This is a silly way of doing this. We could just store a string of the processed characters
    # and then just slice the last 2-4 characters to compare instead of using a queue.
    new_queue = add_to_queue(added_char: char, queue: last_three_char_queue)
    test_two_letter_strings = true if validate_two_letter_strings?(two_letter_matchers:,
                                                                   queue: new_queue)
    test_three_letter_odds_match = true if validate_three_letter_odds_match?(queue: new_queue)
    new_queue.shift if new_queue[0].length == 4
  end
  nice_string_count += 1 if vowels_counter >= 3 && !test_matching_string && test_double_char
  nice_string_count_part_two += 1 if test_two_letter_strings && test_three_letter_odds_match
end

puts nice_string_count
puts nice_string_count_part_two
