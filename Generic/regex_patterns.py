#! python3
# regular expressions
import re
phoneNumRegex = re.compile(r'\d\d-\d{10}')  # compile function return a regex object from the given raw string
""" search function finds regex match in the given string and returns a group,if not found it returns none """
match_ob = phoneNumRegex.search('my number is 91-9492234999')
print('Phone number:'+match_ob.group())
# Adding parenthesis to regex will create groups
phoneNumRegex_groups = re.compile(r'(\d\d)-(\d{10})')
match_ob_g = phoneNumRegex_groups.search('my number is 91-9492234999')
print(match_ob_g.group(1), match_ob_g.group(2),
      match_ob_g.group(0))  # passing 0 or nothing to group returns entire match string
areaCode, main_num = match_ob_g.groups()  # groups func retrieves all the groups
print(f'area code is {areaCode} and main number is {main_num}')

"""
In regex,the following characters have special meanings: 
 .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
If you want to detect these characters as part of your text pattern, you need to escape them with a backslash:
\.  \^  \$  \*  \+  \?  \{  \}  \[  \]  \\  \|  \(  \)

"""
# The | character is called a pipe. You can use it anywhere you want to match one of many expressions.

heroRegex = re.compile(r'Batman|Tony strak')
match_ob_hero = heroRegex.search('Batman and Tony')
print(match_ob_hero.group())

heroRegex = re.compile(r'Bat(man|mobile|cat|dog)')  # when we want to match several patterns
match_ob_shero = heroRegex.search('Batmobile and tony')
print(match_ob_shero.group())

""" Question Mark(?) --> the regex should find a match regardless of whether that bit of text is there
in other words match zero or one"""
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('Batman is ready')
print(mo1.group())
mo2 = batRegex.search('Batwoman is getting ready')
print(mo2.group())

phoneNumRegex = re.compile(r'(\d\d-)?\d{10}')
mo3 = phoneNumRegex.search('my number is 91-9492234999')
print(mo3.group())
mo4 = phoneNumRegex.search('my number is 9492324999')
print(mo4.group())

#  Astrix(*) --> match zero or many
batRegex = re.compile(r'Bat(wo)*man')
mo5 = batRegex.search("Batman")
print(mo5.group())
mo6 = batRegex.search('Batwowowoman')
print(mo6.group())

# Plus(+) --> match one or many
batRegex = re.compile(r'bat(wo)+man')
mo7 = batRegex.search('i\'m batman')  # since it does not have not even one match its return none
print(mo7 == None)

batRegex = re.compile(r'(aa)+')
mo8 = batRegex.findall('aaadaa')
print(mo8)
# caret(^) --> caret in inside the opening bracket of regex makes its negative character class
consoRegex = re.compile(r'[^aeiouAEIOU]')
conso_tuple = consoRegex.findall('this regex will return all the consonants in this sentence')
print(conso_tuple)
"""
1.The regex (Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.

2.While search() will return a Match object of the first matched text in the searched string, 
  the findall() method will return the strings of every match in the searched string and findall() will return a list of tuples
3.\d :0-9
  \w :a-z,A-z,0-9,underscore
  \s :space,tab
4.You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur 
  at the beginning of the searched text.Likewise, you can put a dollar sign ($) at the end of the regex to indicate 
  the string must end with this regex pattern.
5.To make your regex case-insensitive, you can pass re.IGNORECASE or re.I as a second argument to re.compile().
"""
