#Methods to replace values of variables


variable_1 = 1
variable_2 = 2

variable_2 = variable_1
variable_1 = variable_2

#answer will be wrong both 1


#------------------------------------#
#To overcome this issue we use a temporary variable to store value

variable_1 = 1
variable_2 = 2

auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary


#------------------------------------#
#Third and best method


variable_1 = 1
variable_2 = 2

variable_1, variable_2 = variable_2, variable_1
