"""You are in the process of creating a new framework. In order to enhance flexibility, when your user assigns value to an instance attribute, you want to give them the option to supply a callable without arguments instead. When the attribute is accessed, either the assigned value (as usual), or the result of the call (if defined as a callable) should be returned.

Create a class called Setting that supports the 'Optionally callable attribute' pattern.

Details
Only public and private instance attributes should follow the 'Optionally callable attribute' pattern.
Subclassing Setting should work normally, and subclasses will also have to support the "Optionally callable attribute" pattern.
Private properties, class level properties or any kind of methods defined on the class or subclass body won't support the 'Optionally callable attribute' pattern, and these won't be modified at runtime. Note that methods should work normally.
It must be possible to assign 'optionally callable attributes' on different instances of the same class with different values/callables.
'Optionally callable attributes' can be reassigned at any time, callable attributes may be reassigned with non-callable values and vice versa.
The callables may use variables of the scope in which they were defined. They will never make use of the self argument, since they are called with no arguments.
Example
In the code below, we have an instance attribute _pressure storing the current pressure in Pa, and two class attributes unit and unit_multiplier shared by all instances. The pressure is defined as a callable that automatically returns _pressure converted into the correct unit on each access:

class Setting:
    # Your code here
    pass

setting = Setting()
setting._pressure = 101_325
Setting.unit = 'Pa'
Setting.unit_multiplier = {'Pa': 1, 'kPa': 10**3, 'bar': 10**5, 'MPa': 10**6}
setting.pressure = lambda: setting._pressure / Setting.unit_multiplier[Setting.unit]  

Setting.unit = 'Pa'
setting.pressure # -> 101325.0

Setting.unit = 'kPa'
setting.pressure # -> 101.325

Setting.unit = 'bar'
setting.pressure # -> 1.01325

Setting.unit = 'MPa'
setting.pressure # -> 0.101325
Note that in the example above, the lambda function is accessing setting as a variable of the scope at the time of declaration, and not as the actual instance of itself. This is less than ideal, and while it would be possible to make use of the self argument, this is not part of the objectives of your tiny framework."""


# ---------- ANSWER - ->
class Setting:
    pass
