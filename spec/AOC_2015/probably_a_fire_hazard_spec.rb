require_relative '../../AOC_2015/06_probably_a_fire_hazard/probably_a_fire_hazard'
require 'rspec'

describe 'ProbablyAFireHazard' do
  context 'initialize()' do
    it 'initializes array with provided height' do
      greeting = ProbablyAFireHazard.new(height: 3, width: 2)
      expect(greeting.array).to eq([Array.new(2), Array.new(2), Array.new(2)])
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

  context 'handle()' do
    it 'it turns first row on' do
      fire_hazard = ProbablyAFireHazard.new(height: 3, width: 3)
      fire_hazard.handle 'turn on 0,0 through 2,0'
      expect(fire_hazard.array[0]).to eq(
        [1, 1, 1]
      )
      expect(fire_hazard.count_lights).to eq(3)
    end

    it 'it executes 2 commands on same row' do
      fire_hazard = ProbablyAFireHazard.new(height: 3, width: 3)
      fire_hazard.handle 'turn on 0,0 through 2,0'
      fire_hazard.handle 'turn off 1,0 through 1,0'
      expect(fire_hazard.array[0]).to eq(
        [1, nil, 1]
      )
      expect(fire_hazard.count_lights).to eq(2)
    end

    it 'it executes 2 commands on multiple rows row' do
      fire_hazard = ProbablyAFireHazard.new(height: 3, width: 3)
      fire_hazard.handle 'turn on 0,0 through 2,2'
      fire_hazard.handle 'turn off 1,0 through 1,1'
      expect(fire_hazard.array).to eq([
                                        [1, nil, 1],
                                        [1, nil, 1],
                                        [1, 1, 1]
                                      ])
      expect(fire_hazard.count_lights).to eq(7)
    end
  end
end
