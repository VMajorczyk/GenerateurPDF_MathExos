import os
import random
from abc import ABC, abstractmethod
from array import array

import numpy as np

# classe abstraite de base pour générer les formules d'exercices
class Exercise(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def write_header_exo(self, file):
        pass

    @abstractmethod
    def write_content(self, file):
        pass

    @abstractmethod
    def generate_formula(self):
        pass

    existing_calculus = []
    no_new_calculus_count = 0

    def is_existing_calculus_bi2(self, v1, v2, sign=0):
        if self.no_new_calculus_count > 100:
            self.reset_exo()
        for i in self.existing_calculus:
            if i[2] == sign and ((i[0] == v1 and i[1] == v2) or (i[0] == v2 and i[1] == v1)):
                self.no_new_calculus_count = self.no_new_calculus_count + 1
                return True
        self.add_new_calculs_2(v1, v2, sign)
        self.no_new_calculus_count = 0
        return False

    def is_existing_calculus_mono2(self, v1, v2, sign=0):
        if self.no_new_calculus_count > 100:
            self.reset_exo()
        for i in self.existing_calculus:
            if i[2] == sign and i[0] == v1 and i[1] == v2:
                self.no_new_calculus_count = self.no_new_calculus_count + 1
                return True
        self.add_new_calculs_2(v1,v2, sign)
        self.no_new_calculus_count = 0
        return False

    def add_new_calculs_2(self, v1, v2, sign=0):
        row = [v1, v2, sign]
        self.existing_calculus.append(row)
        return

    def reset_exo(self):
        self.existing_calculus = []

# exercice addition de nombre [1; 10] + [1; 3] = [2; 10]
class Exercise01(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_01_10plus3_max10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,10)
            v2 = random.randint(1,3)
            b = random.randint(0, 1)
            if b == 1:
                v1, v2 = v2, v1
            if v1 == self.v1tmp or v2 == self.v2tmp or v1 + v2 > 10:
                continue # try again
            break

        self.v1tmp = v1
        self.v2tmp = v2
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"


# exercice addition de nombre [10; 5] + [1; 5] = [2; 10]
class Exercise02(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_02_10plus5_max10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1, 10)
            v2 = random.randint(1, 5)
            if v1 == self.v1tmp or v2 == self.v2tmp:
                continue # try again
            break

        self.v1tmp = v1
        self.v2tmp = v2
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 10] + [1; 10] = [2; 20]
class Exercise03(Exercise):
    def get_name(self):
        return "CCM_Calcul_03_10plus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,10)
            v2 = random.randint(1,10)
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 10] + [1; 10] + [1; 10] = [3; 30]
class Exercise04(Exercise):
    def get_name(self):
        return "CCM_Calcul_04_10plus10plus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 20, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_20_2col(file, self)
        LatexGenerator.write_footer_20(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,10)
            v2 = random.randint(1,10)
            v3 = random.randint(1, 10)
            if self.is_existing_calculus_bi2(v1,v2,v3):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "+" + str(v3) + "$&$= \\dotfill $"

 # exercice addition de nombre [1; 10] + [1; 10] = [2; 20]
 #      et complement de 10 => 10 - [1; 10] = [9; 0]
 # favorise les résultats > 7
class Exercise05(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_05_10plus10_compl10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        b = random.randint(0, 4)

        while True:
            v1 = random.randint(1, 10)
            v2 = random.randint(1, 10)

            if self.is_existing_calculus_bi2(v1,v2, b):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2, b)
        if b == 0:
            return "$10-" + str(v2) + "$&$= \\dotfill $"
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 30] + [1; 10] = [2; 40]
class Exercise06(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_06_30plus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 4)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,30)
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            if b==1:
                v1,v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 100] + [1; 10] = [2; 100]
class Exercise07(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_07_100plus10_max100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 4)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1, 99)
            v2 = random.randint(1, 10)
            b = random.randint(0, 1)
            if b == 1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2) or v1 + v2 > 99:
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 100] + [1; 20] = [2; 100]
class Exercise08(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_08_100plus20_max100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 4)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,20)
            b = random.randint(0,1)
            if b==1:
                v1,v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2) or v1 + v2 > 99:
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice addition de nombre [1; 100] + [1; 20] = [2; 100]
class Exercise09(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_09_100plus100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 4)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,99)

            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "+" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 10] - [1; 10] = [0; 9]
class Exercise10(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_10_10minus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,10)
            v2 = random.randint(1,10)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "-" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 19] - [1; 10] = [0; 19]
class Exercise11(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_11_19minus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,19)
            v2 = random.randint(1,10)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "-" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 100] - [1; 10] = [0; 99]
class Exercise12(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_12_100minus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,10)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "-" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 100] - [1; 20] = [0; 99]
class Exercise13(Exercise):

    def get_name(self):
        return "CCM_Calcul_13_100minus20"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,20)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "-" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 100] - [1; 100] = [0; 99]
class Exercise14(Exercise):

    def get_name(self):
        return "CCM_Calcul_14_100minus100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,99)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)
        return "$" + str(v1) + "-" + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 20] - [1; 10] = [0; 19]
#       addition [1; 10] + [1; 10] = [1; 20]
class Exercise15(Exercise):
    signtmp = 0

    def get_name(self):
        return "CCM_Calcul_15_10plus10_20minus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        # sign==0 => +
        # sign==1 => -
        sign = random.randint(0, 1)
        if sign == 0:
            maxv1 = 10
        else:
            maxv1 = 20

        while True:
            v1 = random.randint(1,maxv1)
            v2 = random.randint(1,10)
            if sign == 1 and v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2, sign) and (sign == self.signtmp):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2,sign)
        self.signtmp = sign
        if sign==0:
            signchar = "+"
        else:
            signchar = "-"
        return "$" + str(v1) + signchar + str(v2) + "$&$= \\dotfill $"

# exercice soustraction de nombre [1; 100] - [1; 10] = [0; 99]
#       addition [1; 100] + [1; 10] = [1; 100]
class Exercise16(Exercise):
    signtmp = 0

    def get_name(self):
        return "CCM_Calcul_16_100plus10_100minus10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        # sign==0 => +
        # sign==1 => -
        sign = random.randint(0, 1)

        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,10)
            if sign == 1 and v2 > v1:
                v1, v2 = v2, v1
            if sign == 0 and v1+v2 > 100:
                b = random.randint(0,1)
                if b==1:
                    v1,v2 = v2,v1
                continue # try again
            if self.is_existing_calculus_bi2(v1,v2, sign) and (sign == self.signtmp):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2,sign)
        self.signtmp = sign
        if sign==0:
            signchar = "+"
        else:
            signchar = "-"
        return "$" + str(v1) + signchar + str(v2) + "$&$= \\dotfill $"

# exercice additions posées de nombre [1; 100] + [1; 10] = [0; 99]
#       addition [1; 100] + [1; 10] = [1; 100]
class Exercise17(Exercise):
    def get_name(self):
        return "CCM_Calcul_17_100plus100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 20, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_20_5col(file, self)
        LatexGenerator.write_footer_20(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,99)
            v2 = random.randint(1,99)
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)

        # add space between figures
        strv1 = ""
        while v1 != 0:
            strv1 = str(v1%10) + "\\:" + strv1
            v1 = v1//10

        # add space between figures
        strv2 = ""
        while v2 != 0:
            strv2 = str(v2%10) + "\\:" + strv2
            v2 = v2//10

        return "$ \\begin{array}{r} \\phantom{+0}" + strv1 + " \\\\ + \\phantom{0}"+ strv2 + " \\\\ \\hline \\dotfill \\end{array} $"

# exercice soustraction de nombre [1; 100] - [1; 100] = [0; 99]
class Exercise18(Exercise):

    def get_name(self):
        return "CCM_Calcul_18_100minus100"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 20, 3)
        return

    def write_content(self, file):
        LatexGenerator.write_table_20_5col(file, self)
        LatexGenerator.write_footer_20(file)
        return

    def generate_formula(self):
        while True:
            v1 = random.randint(1,100)
            v2 = random.randint(1,100)
            if v2 > v1:
                v1, v2 = v2, v1
            if self.is_existing_calculus_bi2(v1,v2):
                continue # try again
            break

        self.add_new_calculs_2(v1,v2)

        strv1 = ""
        while v1 != 0:
            strv1 = str(v1%10) + "\\:" + strv1
            v1 = v1//10

        strv2 = ""
        while v2 != 0:
            strv2 = str(v2%10) + "\\:" + strv2
            v2 = v2//10

        return "$ \\begin{array}{r} \\phantom{-0}" + strv1 + " \\\\ - \\phantom{0}" + strv2 + " \\\\ \\hline \\dotfill \\end{array} $"

# exercice multiplication x2 [2] * [1; 10] = [1; 20]
class Exercise19(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_19_2mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = 2
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x3 [3] * [1; 10] = [1; 20]
class Exercise20(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_20_3mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = 3
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x2 à x3 [2; 3] * [1; 10] = [1; 20]
class Exercise21(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_21_2-3mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = random.randint(2,3)
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x4 [4] * [1; 10] = [1; 20]
class Exercise22(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_22_4mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = 4
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x2 à x4 [2; 4] * [1; 10] = [1; 20]
class Exercise23(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_23_2-4mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = random.randint(2,4)
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x5 [5] * [1; 10] = [1; 20]
class Exercise24(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_24_5mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = 5
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x2 à x5 [2; 5] * [1; 10] = [1; 20]
class Exercise25(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_25_2-5mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = random.randint(2,5)
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# exercice multiplication x2 à x5 [2; 5] * [1; 10] = [1; 20]
class Exercise26(Exercise):
    v1tmp = 0
    v2tmp = 0

    def get_name(self):
        return "CCM_Calcul_26_2or5mul10"

    def write_header_exo(self, file):
        LatexGenerator.write_header_exo(file, 40, 5)
        return

    def write_content(self, file):
        LatexGenerator.write_table_40_3col(file, self)
        LatexGenerator.write_footer_40(file)
        return

    def generate_formula(self):
        while True:
            v0 = v1 = random.randint(2,3)
            if v0 == 3:
                v0 = v1 = 5
            v2 = random.randint(1,10)
            b = random.randint(0,1)
            c = random.randint(1, 4)
            if b==1 & c <= 2:
                v1,v2 = v2, v1
            if c > 2:
                b = 2
            if self.is_existing_calculus_bi2(v1,v2,b):
                continue # try again
            break

        v3 = v1 * v2

        self.add_new_calculs_2(v1,v2, b)

        if c <= 2:
            return "$ " + str(v1) + " \\times " + str(v2) + " $&$= \\ldots $"
        elif c == 3:
            return "$ "+ str(v0) +" \\times \\ldots $&$= " + str(v3) + " $"
        else: # c == 4:
            return "$ \\ldots  \\times "+ str(v0) +" $&$= " + str(v3) + " $"

# produit le document d'exercice
class LatexGenerator:
    def __init__(self):
        self.exo = Exercise01()

    def generate_formula(self):
        return self.exo.generate_formula()

    pagebegin = """    % table principale avec opérations
    \\begin{table}[ht]
    \\Large
    \\centering
    \\begingroup\n"""

    pageend3 = """    \\end{tabular}
    \\endgroup
    \\end{table}
    % information sur les scores
    \\subsection*{Score}
    \\begin{figure}[h!]
    \\begin{minipage}{0.45\\linewidth}
    %    tableau des ceintures
    \\begin{tabular}{|c|c|}
    \\hline
    Ceinture & Score \\\\
    \\hline
    Blanche & 0 à 10\\\\
    \\cellcolor{LemonChiffon1}Jaune & 11 à 15\\\\
    \\cellcolor{LightSalmon1}Orange & 16 à 20\\\\
    \\cellcolor{DarkSeaGreen1}Verte & 21 à 25\\\\
    \\cellcolor{LightBlue1}Bleue & 26 à 30\\\\
    \\cellcolor{Bisque4}Marron & 31 à 35\\\\
    \\cellcolor{Honeydew4}\\textcolor{white}{Noire} & 36 à 39\\\\
    \\cellcolor{Tomato1}\\textcolor{white}{Rouge} & \\cellcolor{Tomato1}\\textcolor{white}{40}\\\\
    \\hline
    \\end{tabular}
    \\end{minipage}
    \\begin{minipage}{0.45\\linewidth}
    % tableau du score de l'enfant
    \\begin{tabular}{|ll|}
    \\hline
    Calculs effectués: & $\\qquad$ \\\\
    Calculs faux: & $\\qquad$ \\\\
    Calculs corrects: & $\\qquad$ \\\\
    \\hline
    \\end{tabular}
    % dessin de la ceinture à colorier
    \\includegraphics[width = 4cm]{judo_belt.png}
    \\end{minipage}
    \\end{figure}
    \\newpage\n"""

    pageend2 = """    \\end{tabular}
    \\endgroup
    \\end{table}
    % information sur les scores
    \\subsection*{Score}
    \\begin{figure}[h!]
    \\begin{minipage}{0.45\\linewidth}
    %    tableau des ceintures
    \\begin{tabular}{|c|c|}
    \\hline
    Ceinture & Score \\\\
    \\hline
    Blanche & 0 à 5\\\\
    \\cellcolor{LemonChiffon1}Jaune & 6 à 8\\\\
    \\cellcolor{LightSalmon1}Orange & 9 à 11\\\\
    \\cellcolor{DarkSeaGreen1}Verte & 12,13\\\\
    \\cellcolor{LightBlue1}Bleue & 14,15\\\\
    \\cellcolor{Bisque4}Marron & 16,17\\\\
    \\cellcolor{Honeydew4}\\textcolor{white}{Noire} & 18,19\\\\
    \\cellcolor{Tomato1}\\textcolor{white}{Rouge} & \\cellcolor{Tomato1}\\textcolor{white}{20}\\\\
    \\hline
    \\end{tabular}
    \\end{minipage}
    \\begin{minipage}{0.45\\linewidth}
    % tableau du score de l'enfant
    \\begin{tabular}{|ll|}
    \\hline
    Calculs effectués: & $\\qquad$ \\\\
    Calculs faux: & $\\qquad$ \\\\
    Calculs corrects: & $\\qquad$ \\\\
    \\hline
    \\end{tabular}
    % dessin de la ceinture à colorier
    \\includegraphics[width = 4cm]{judo_belt.png}
    \\end{minipage}
    \\end{figure}
    \\newpage\n"""

    @staticmethod
    def write_table_20_5col(file, exo):
        file.write("\\begin{tabular}{p{2cm}p{2cm}p{2cm}p{2cm}p{2cm}}\n")
        for i in range(4):
            file.write(exo.generate_formula() + "\\vspace{10pt}&" + exo.generate_formula() + "&" + exo.generate_formula() + "&" + exo.generate_formula() + "&" + exo.generate_formula() + "\\\\ \n")
        return

    @staticmethod
    def write_table_40_3col(file, exo):
        file.write("\\begin{tabular}{p{1.5cm}p{1.8cm}p{1.5cm}p{1.8cm}p{1.5cm}p{1.8cm}}\n")
        for i in range(13):
            file.write(exo.generate_formula() + "&" + exo.generate_formula() + "&" + exo.generate_formula() + "\\\\\n")
        file.write(exo.generate_formula() + "& & & & \n")
        return

    @staticmethod
    def write_table_20_2col(file, exo):
        file.write("\\begin{tabular}{p{3cm}p{1.8cm}p{3cm}p{1.8cm}}\n")
        for i in range(10):
            file.write(exo.generate_formula() + "&" + exo.generate_formula() + "\\\\\n")
        return

    @staticmethod
    def write_header_exo(file, nb_calculus, nb_minutes):
        file.write("    \\section*{Calculs Contre la Montre}\n")
        file.write("    \\subsection*{Faire les "+ str(nb_calculus) +" calculs en "+ str(nb_minutes) +" minutes}\n")
        return

    @staticmethod
    def write_footer_20(file):
        file.write(LatexGenerator.pageend2)
        return

    @staticmethod
    def write_footer_40(file):
        file.write(LatexGenerator.pageend3)
        return

    def write_page(self, file):
        self.exo.write_header_exo(file)
        file.write(self.pagebegin)
        self.exo.write_content(file)
        self.exo.reset_exo()


    def write_document(self, exercise, page_number:100):
        self.exo = exercise
        with open("genfile.tex", 'w', encoding='utf-8') as file:
            file.write("\\documentclass[a5paper]{article}\n")
            file.write("\\usepackage[utf8]{inputenc}\n")
            file.write("\\usepackage[T1]{fontenc}\n")
            file.write("\\usepackage[french]{babel}\n")
            file.write("\\usepackage{amsmath}\n")
            file.write("\\usepackage{graphicx}\n")
            file.write("\\usepackage{fancyhdr}\n")
            file.write("\\usepackage{hyperref}\n")
            file.write("\\usepackage[hmargin=1cm, top=2cm, bottom=2cm]{geometry}\n")
            file.write("\\usepackage[table, x11names]{xcolor}\n")
            file.write("\\pagestyle{fancy}\n")
            file.write("\\fancyhf{}")
            file.write("\\chead{\\url{https://github.com/VMajorczyk/GenerateurPDF_MathExos}}")
            file.write("\\cfoot{\\thepage}")

            file.write("\\begin{document}\n")

            for i in range(page_number):
                self.write_page(file)

            file.write("\\end{document}\n")

        input_file = 'genfile.tex'
        output_file = self.exo.get_name()
        if not os.path.exists("./output"):
            os.makedirs("./output")
        os.system("pdflatex genfile.tex -jobname=./output/" + output_file)

lg = LatexGenerator()

nb_pages = 100

if True:
    lg.write_document(Exercise01(), nb_pages)
    lg.write_document(Exercise02(), nb_pages)
    lg.write_document(Exercise03(), nb_pages)
    lg.write_document(Exercise04(), nb_pages)
    lg.write_document(Exercise05(), nb_pages)
    lg.write_document(Exercise06(), nb_pages)
    lg.write_document(Exercise07(), nb_pages)
    lg.write_document(Exercise08(), nb_pages)
    lg.write_document(Exercise09(), nb_pages)
    lg.write_document(Exercise10(), nb_pages)
    lg.write_document(Exercise11(), nb_pages)
    lg.write_document(Exercise12(), nb_pages)
    lg.write_document(Exercise13(), nb_pages)
    lg.write_document(Exercise14(), nb_pages)
    lg.write_document(Exercise15(), nb_pages)
    lg.write_document(Exercise16(), nb_pages)
    lg.write_document(Exercise17(), nb_pages)
    lg.write_document(Exercise18(), nb_pages)
    lg.write_document(Exercise19(), nb_pages)
    lg.write_document(Exercise20(), nb_pages)
    lg.write_document(Exercise21(), nb_pages)
    lg.write_document(Exercise22(), nb_pages)
    lg.write_document(Exercise23(), nb_pages)
    lg.write_document(Exercise24(), nb_pages)
    lg.write_document(Exercise25(), nb_pages)
    lg.write_document(Exercise26(), nb_pages)