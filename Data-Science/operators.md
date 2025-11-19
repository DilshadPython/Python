{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d115792d-5095-4328-a403-9e9f4b0aaa81",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 'H'\n",
    "b = 22\n",
    "f = 2.3\n",
    "c = 3j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "648929fa-5bec-4f03-8591-d46270a2d033",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Variable   Type       Data/Info\n",
      "-------------------------------\n",
      "a          str        H\n",
      "b          int        22\n",
      "c          complex    3j\n",
      "f          float      2.3\n"
     ]
    }
   ],
   "source": [
    "%whos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "62727028-1e37-4c3f-a06b-ba23badc8808",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\t b\t c\t f\t \n"
     ]
    }
   ],
   "source": [
    "%who"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "b72bc9cd-41f6-4213-8e13-d99b1f1a3a68",
   "metadata": {},
   "outputs": [],
   "source": [
    "sumOfbAndf = b + c"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4d35e18f-f4c1-45ec-93f6-48c38dca4116",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(22+3j)"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sumOfbAndf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "de3db9a9-87ce-417c-8506-16c5b5038122",
   "metadata": {},
   "outputs": [],
   "source": [
    "sumOfbAndf = b+f"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "474ec9c3-78e5-4e49-8eb8-6cb3d8d5f52b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24.3"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sumOfbAndf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "73b09bd4-f939-47c8-8cb6-e74f16014ddd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "24.3"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "7619a803-342b-4123-b000-7269e1f9c4d3",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid decimal literal (3434516666.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[22]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m3x = 4\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid decimal literal\n"
     ]
    }
   ],
   "source": [
    "3x = 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "c580b705-b644-43b2-83b4-9da1f319ee8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "d2 = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "1b11a50a-f054-4fe7-a9d7-aa2e3b091a51",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "starred assignment target must be in a list or tuple (3440009485.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[24]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m*t = 33\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m starred assignment target must be in a list or tuple\n"
     ]
    }
   ],
   "source": [
    "*t = 33"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "5e0c70a2-90a0-4b6c-9dbd-f9fe42dcbe8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "_f = 88"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "da1e2a75-3497-4058-9489-d4d842a2d89a",
   "metadata": {},
   "outputs": [],
   "source": [
    "_g = 'Google'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "8c15ff76-d1fb-4e33-839f-4ff0ea57afd5",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "cannot assign to expression here. Maybe you meant '==' instead of '='? (976543351.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[27]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31ma | b | c = 'Hello Dill'\u001b[39m\n    ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m cannot assign to expression here. Maybe you meant '==' instead of '='?\n"
     ]
    }
   ],
   "source": [
    "a | b | c = 'Hello Dill'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "534232c2-e7bb-406f-ac3f-250cb8d59682",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1772206145.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[28]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m4 !> 5\u001b[39m\n      ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "4 !> 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "47551543-3a29-4e45-9850-afe0b587aa18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not True is False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "1d2d2f50-c3a5-4c48-9f34-f6ee8a1cf587",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not False is True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "b2d77417-312d-4452-8bb8-b01a7bb7636e",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (3253877897.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[31]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31mTrue is ==\u001b[39m\n            ^\n\u001b[31mSyntaxError\u001b[39m\u001b[31m:\u001b[39m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "True is == "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "ca84d45f-b0cd-49bf-b16b-ef6707bbec7c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "a\t aumOfbAndf\t b\t c\t d2\t f\t sumOfbAndf\t \n"
     ]
    }
   ],
   "source": [
    "%who"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "2b4afce0-6189-44d1-b980-d18c3bc3a90f",
   "metadata": {},
   "outputs": [],
   "source": [
    "a = True\n",
    "b = True\n",
    "c = False"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "9cd7a872-19b0-4b56-a52f-184eb0e194e2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(a and b)\n",
    "print(a and c)\n",
    "print(c and b)\n",
    "print(b and a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "c7391aa7-0ae2-4f56-91b3-8becff6bf180",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = True\n",
    "y = False\n",
    "z = False\n",
    "w = True"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "9bd9040d-d212-43db-a55d-94b9d1053290",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print(x or w)\n",
    "print(x or y)\n",
    "print(z or w)\n",
    "print(y or z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "39c7b0af-9b96-48b3-8410-5d89860e6af2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "f57f5e83-cfd0-412c-9e40-dec3d9b3f0ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "41dc3c8e-ef24-4983-81fc-c67bfd5aa0d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "3dffd7cb-ac8d-4f4b-903d-8a474c7ef9b7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "f4e304cf-9f19-4e1f-ae5d-c4ce875172d4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not((x and w) or (y and z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "6a18f008-b419-420e-8b21-c5098d023837",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not((x and w))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "4b5eb3d7-68c2-4a30-920f-a3134460e719",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not((y and z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "2d617ebc-32df-424b-a8a0-7716df29586a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(x or w)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "0e9b4452-8d3d-4228-9b1d-6e57bf27f0ad",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not(y or z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "c900d7d7-cc64-4e1f-b4ef-ba27910e19e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "e = 5\n",
    "g = 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "33b4105e-e561-4eb6-840f-3de6643630c0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e == g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "a04d0ffb-c3b8-4c93-9c32-c8d8e3551434",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e != g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "b606f6c9-d8ca-4302-a238-5d664aa22465",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e <= g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "56382206-d489-4dfa-b9e5-e339b6fa3513",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "e >= g"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6f3c06d-253b-421f-b76f-9dc57199d8f0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
