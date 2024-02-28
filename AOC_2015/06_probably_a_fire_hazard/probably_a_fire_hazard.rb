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

  def initialize(height)
    @array = Array.new(height) { Array.new(0) }
  end

  def self.parse(string)
    unless /(?<operation>(turn on|turn off|toggle)) (?<start_coords>(\b\d{1,3},\d{1,3})\b) through (?<end_coords>(\b\d{1,3},\d{1,3})\b)/ =~ string
      return
    end

    Instruction.new operation:, start_coords: start_coords.split(',').map(&:to_i),
                    end_coords: end_coords.split(',').map(&:to_i)
  end

  end
end
