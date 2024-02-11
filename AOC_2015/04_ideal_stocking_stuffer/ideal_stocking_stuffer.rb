require 'digest'

# Do a while loop to find the hash that starts with 5 zeros
def hash_starts_with_zeros(num:)
  i = -1
  hash = ''
  while hash[0..num - 1] != 0.to_s * num
    i += 1
    hash = Digest::MD5.hexdigest 'bgvyzdsv' + i.to_s
  end
  puts "#{i} has a hash of #{hash}"
end
# For each chop the first 5 characters and compare with '00000'
# If it is not equal, increment the number and try again
puts hash_starts_with_zeros num: 5
