import unittest, re
from apiProject import user_inputLink, get_json, heardcoded_apiInfo, create_dic

class TestFileName(unittest.TestCase):
    def test_function1(self):
        string_val = user_inputLink()
        
        self.assertTrue(len(string_val) > 20)
        
        special_char_isTrue = False
        special_char = re.compile('[@_!#$%^&*()<>?/\|}{~:]')       
        if(special_char.search(string_val) != None):
          special_char_isTrue = True
        self.assertTrue(special_char_isTrue)
        
        nums_res = any(chr.isdigit() for chr in string_val)
        self.assertTrue(nums_res)
        
        has_upper_case = any(chr.upper() for chr in string_val)
        self.assertTrue(has_upper_case)
        
        has_lower_case = any(chr.lower() for chr in string_val)
        self.assertTrue(has_lower_case)

    def test_function2(self):
        string_val = user_inputLink()
        is_json = get_json(string_val, heardcoded_apiInfo())
        self.assertTrue(type(is_json), dict)
        
    def test_function3(self):
        string_val = user_inputLink()
        jsonformat = get_json(string_val, heardcoded_apiInfo())
        dic_list = create_dic(jsonformat)
        key_list = dic_list.keys()


        contains_names = False 
        contains_geners = False
        contains_pop_score = False

        if 'name' in key_list:
          contains_names = True
          
        if 'popularity' in key_list:
          contains_pop_score = True
          
        if 'genres' in key_list:
          contains_geners = True
          
        self.assertTrue(type(dic_list), dict)
        self.assertTrue(contains_names)
        self.assertTrue(contains_geners)
        self.assertTrue(contains_pop_score)
          
        

      

if __name__ == '__main__':
    unittest.main()