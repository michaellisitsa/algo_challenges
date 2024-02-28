require_relative '../../AOC_2015/06_probably_a_fire_hazard/probably_a_fire_hazard'
require 'rspec'

describe 'ProbablyAFireHazard' do
  context 'initialize()' do
    it 'initializes array with provided height' do
      greeting = ProbablyAFireHazard.new(3)
      expect(greeting.array).to eq([[], [], []])
    end
  end

  context 'parse()' do
    it 'interprets on and off instructions' do
      parsed = ProbablyAFireHazard.parse 'turn on 0,0 through 999,999'
      expect(parsed.to_h).to include(
        operation: 'turn on',
        start_coords: [0, 0],
        end_coords: [999, 999]
      )
      # expect(parsed.to_h).to eq(['turn on', [0, 0], [999, 999]])
    end
    it 'interprets on and off instructions' do
      parsed = ProbablyAFireHazard.parse 'turn off 0,0 through 999,999'
      expect(parsed.to_h).to include(
        operation: 'turn off'
      )
    end
    it 'returns nothing for invalid instructions' do
      parsed = ProbablyAFireHazard.parse 'something else 0,0 through 999,999'
      expect(parsed).to be(nil)
    end
  end
  end
end
