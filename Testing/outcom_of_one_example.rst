> /home/dillmac/Devel/Python/Testing/using_pdb_to_test.py(12)<module>()
-> values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb

(Pdb) rv
*** Not yet returned!
(Pdb) s
> /home/dillmac/Devel/Python/Testing/using_pdb_to_test.py(14)<module>()
-> myresult = 0
(Pdb) key
*** NameError: name 'key' is not defined
(Pdb) myresult
*** NameError: name 'myresult' is not defined
(Pdb) n
> /home/dillmac/Devel/Python/Testing/using_pdb_to_test.py(16)<module>()
-> for key in values:
(Pdb) key
*** NameError: name 'key' is not defined
(Pdb) h

Documented commands (type help <topic>):
========================================
EOF    c          d        h         list      q        rv       undisplay
a      cl         debug    help      ll        quit     s        unt      
alias  clear      disable  ignore    longlist  r        source   until    
args   commands   display  interact  n         restart  step     up       
b      condition  down     j         next      return   tbreak   w        
break  cont       enable   jump      p         retval   u        whatis   
bt     continue   exit     l         pp        run      unalias  where    

Miscellaneous help topics:
==========================
exec  pdb