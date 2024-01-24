# Function implementation
my_list = open('not_quite_lisp/data.txt', &:readline).split('')
current_position = 1
result = 0
while current = my_list.shift
  result = current == '(' ? result + 1 : result - 1
  @basement_entered ||= current_position if result == -1
  current_position += 1
end
puts result
puts @basement_entered
