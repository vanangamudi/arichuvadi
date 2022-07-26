* அரிச்சுவடி - Arichuvadi
இந்த பைத்தான் பொதி, தமிழ்ச்சரங்ளை எழுத்துக்களாக நறுக்கும் மிகவெளிய வேலையைச்செய்ய உதவும். 
This packages was written as part of regex engine from scratch for tamil. It provides very basic functionalities such as splitting the string into characters inline with how a native Tamil speakers thinks. Open-Tamil package by contrast provides a myriad of utilities to deal with Tamil text. 

*  எடு.கா.:
#+begin_src python
  # -*- coding: utf-8 -*-
  import arichuvadi as ari
  saram = 'The Great உயர்தனிச்செம்மொழி தமிழ்!!!'
  print(1, saram)
  print(2, list([i for i in saram]))
  print(3, ari.get_letters_coding(saram))
  print(4, ari.get_letters_glyph(saram))
#+end_src

#+RESULTS:
1 The Great உயர்தனிச்செம்மொழி தமிழ்!!!
2 [T, h, e,  , G, r, e, a, t,  , உ, ய, ர, ், த, ன, ி, ச, ், ச, ெ, ம, ், ம, ொ, ழ, ி,  , த, ம, ி, ழ, ், !, !, !]
3 [T, h, e,  , G, r, e, a, t,  , உ, ய, ர், த, னி, ச், செ, ம், மொ, ழி,  , த, மி, ழ், !, !, !]
4 [T, h, e,  , G, r, e, a, t,  , உ, ய, ர், த, னி, ச், செ, ம், மொ, ழி,  , த, மி, ழ், !, !, !]

