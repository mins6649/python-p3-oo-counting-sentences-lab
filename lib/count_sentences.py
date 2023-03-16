#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value
  
  def get_value(self):
    return self._value
  def set_value(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
  value = property(get_value, set_value)

  def is_sentence(self):
    if self.value[-1] == ("."):
      return True
    else:
      return False
  def is_question(self):
    if self.value[-1] == ("?"):
      return True
    else:
      return False
  def is_exclamation(self):
    if self.value[-1] == ("!"):
    # .endswith() method will also work
      return True
    else:
      return False
  def count_sentences(self):
    replaced_with = self.value.replace("!", ".")
    sentence = replaced_with.replace("?", ".")
    new_sentence = [word for word in sentence.split(".") if word]
    print(new_sentence)
    return(len(new_sentence))

    for punc in ["!","?"]:
      x = self.value.replace(punc, ".")
      sentences = [word for  word in x.split(".") if word]
    print(sentences)
    return len(sentences)
    # THE PUNC ONLY REPLACES ONE ! or ? AT A TIME
      
