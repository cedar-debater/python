class PythonThing(object):
  def set_attributes(self, *args, **kwargs):
    self.attribute_template = "self.%s = %s"
		self.at = self.attribute_template
		for i in kwargs:
      g = i; x = kwargs[i] ## format {g:x}
			exec template%(g, x)
		self.type = PythonThing
class Class(PythonThing):
	def list_to_str(self, the_list, joining_string=", "):
		return joining_string.join(the_list)
	def __init__(self, class_name, parameters, init_code, inheriting=[]):
		template = "class %s(%s):\n\tdef __init__(%s):\n\t%s"
		str_param = self.list_to_str(parameters)
		str_inherit = self.list_to_str(inheriting)
		exec template%(class_name, str_inherit, str_param, init_code)
		exec "self.class_name = %s"%class_name
	def my_class(self):
		return self.class_name
Person = Class("Person", ["self", "first_name", "last_name", "date_of_birth_in_words","date_of_birth_with_slashes" "notes"], "\tpass", []).my_class()
Person_type = type(Person)
print Person_type ## Person MUST be a class
