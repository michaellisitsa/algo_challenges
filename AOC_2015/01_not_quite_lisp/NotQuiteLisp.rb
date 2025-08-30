# Class implementation
class NotQuiteLisp
  attr_reader :delivery_floor, :basement_entered

  def initialize
    @delivery_floor = 0
    my_list = open('not_quite_lisp/data.txt', &:readline).split('')
    current_position = 1

    while current = my_list.shift
      @delivery_floor = current == '(' ? @delivery_floor + 1 : @delivery_floor - 1
      @basement_entered ||= current_position if @delivery_floor == -1
      current_position += 1
    end
  end
end

not_quite_lisp = NotQuiteLisp.new
puts not_quite_lisp.delivery_floor
puts not_quite_lisp.basement_entered
