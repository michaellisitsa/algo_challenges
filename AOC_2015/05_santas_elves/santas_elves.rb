VOWELS = %w[a e i o u]
FORBIDDEN_LETTER_COMBINATIONS = {
  "a": 'b',
  "c": 'd',
  "p": 'q',
  "x": 'y'
}

nice_string_count = 0
File.foreach('AOC_2015/05_santas_elves/data.txt') do |line|
  double_next_char = nil
  matching_next_char = nil

  test_double_char = false
  test_matching_string = false
  vowels = 0
  line.each_char do |_char|
    vowels += 1 if VOWELS.include?(_char)
    test_matching_string = true if matching_next_char == _char
    matching_next_char = FORBIDDEN_LETTER_COMBINATIONS[_char.to_sym]
    test_double_char = true if double_next_char == _char
    double_next_char = _char
  end
  nice_string_count += 1 if vowels >= 3 && !test_matching_string && test_double_char
end

print nice_string_count
