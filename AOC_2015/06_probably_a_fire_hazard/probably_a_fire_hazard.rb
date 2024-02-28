# frozen_string_literal: true


Instruction = Struct.new(:operation, :start_coords, :end_coords, keyword_init: true) do
  def x_range
    start_coords[0]..end_coords[0]
  end

  def y_range
    start_coords[1]..end_coords[1]
  end
end

# My documentation
class ProbablyAFireHazard
  attr_accessor :array

  def initialize(height:, width:)
    # Use an sorted set so we only track the flipped switches rather than the whole row
    @array = Array.new(height) { Array.new(width) }
  end

  def count_lights
    @array.flatten.compact.size
  end


  def self.parse(string)
    unless /(?<operation>(turn on|turn off|toggle)) (?<start_coords>(\b\d{1,3},\d{1,3})\b) through (?<end_coords>(\b\d{1,3},\d{1,3})\b)/ =~ string
      return
    end

    Instruction.new operation:, start_coords: start_coords.split(',').map(&:to_i),
                    end_coords: end_coords.split(',').map(&:to_i)
  end

  def handle(string)
    instruction = self.class.parse(string)
    case instruction.operation
    when 'turn on'
      # For every row in the range instruction.y_range:
      # Set the begin as "on"
      # Set the end as "off"
      # Clear all values in between "on" and "off"
      instruction.y_range.each do |row_idx|
        @array[row_idx].fill(1, instruction.x_range)
      end
    when 'turn off'
      instruction.y_range.each do |row_idx|
        @array[row_idx].fill(nil, instruction.x_range)
      end
    when 'toggle'
      instruction.y_range.each do |row_idx|
        @array[row_idx].map do
          instruction.x_range.each { |col_idx| @array[row_idx][col_idx] = @array[row_idx][col_idx] == 1 ? nil : 1 }
        end
      end
    end
  end
end
