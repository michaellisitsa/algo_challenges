INPUT = 1_113_222_113

def next_look_and_say(input)
  chunks = input.to_s.chars.chunk(&:itself)
  chunks.map do |matcher, chunk|
    "#{chunk.size}#{matcher}"
  end.join
end

def look_and_say(input, *iterations)
  iterations.sort!
  times = {}
  iterations.last.times do |time|
    input = next_look_and_say(input)
    times[time + 1] = input.size if iterations.include?(time + 1)
  end
  times
end

puts look_and_say(1_113_222_113, 50, 40)
