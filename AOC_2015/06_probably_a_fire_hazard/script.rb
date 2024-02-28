require_relative './probably_a_fire_hazard'

fire_hazard = ProbablyAFireHazard.new(height: 1000, width: 1000)
File.foreach('AOC_2015/06_probably_a_fire_hazard/test_data.txt') do |line|
  puts "line: #{line}"
  fire_hazard.handle(line)
end
puts fire_hazard.count_lights
fire_hazard.handle 'turn on 0,0 through 2,0'
