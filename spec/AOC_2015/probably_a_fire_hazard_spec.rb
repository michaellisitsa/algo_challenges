require_relative '../../AOC_2015/06_probably_a_fire_hazard/probably_a_fire_hazard'
require 'rspec'

describe ProbablyAFireHazard do
  context 'Greet' do
    it 'says hello' do
      expect(described_class.start).to eq('hello')
    end
  end
end
