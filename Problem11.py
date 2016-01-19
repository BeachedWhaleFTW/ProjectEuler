# Find largest product of any 4 numbers in a row in this 20 x 20 matrix

line1 = [8, 2, 22, 97, 38, 15, 0, 4, 0, 75, 4, 5, 7, 78, 52, 12, 5, 77, 91, 8]
line2 = [49, 49, 99, 4, 17, 81, 18, 57, 6, 87, 17, 4, 98, 43, 69, 48, 4, 56, 62, 0]
line3 = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 4, 67, 53, 88, 3, 3, 49, 13, 36, 65]
line4 = [52, 7, 95, 23, 4, 6, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
line5 = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 4, 4, 28, 66, 33, 13, 8]
line6 = [24, 47, 32, 6, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 2, 35, 17, 12, 5]
line7 = [32, 98, 81, 28, 64, 23, 67, 1, 26, 38, 4, 67, 59, 54, 7, 66, 18, 38, 64, 7]
line8 = [67, 26, 2, 68, 2, 62, 12, 2, 95, 63, 94, 39, 63, 8, 4, 91, 66, 49, 94, 21]
line9 = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
line10 = [21, 36, 23, 9, 75, 0, 76, 44, 2, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
line11 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 8, 4, 62, 16, 14, 9, 53, 56, 92]
line12 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
line13 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 6, 21, 58, 51, 54, 17, 58]
line14 = [19, 8, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 4]
line15 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
line16 = [88, 36, 68, 87, 57, 62, 2, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
line17 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 4, 62, 76, 36]
line18 = [2, 69, 36, 41, 72, 3, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
line19 = [2, 73, 35, 29, 78, 31, 9, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
line20 = [1, 7, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

list_of_lines = [line1, line2, line3, line4, line5, line6, line7, line8, line9, line10, line11, line12, line13, line14,
                 line15, line16, line17, line18, line19, line20]


def diag_down_right(list_of_rows):
    product = 1
    product_max = 1
    for i in range(17):
        for j in range(17):
            product = list_of_rows[i][j]
            product *= list_of_rows[i + 1][j + 1]
            product *= list_of_rows[i + 2][j + 2]
            product *= list_of_rows[i + 3][j + 3]
            if product > product_max:
                product_max = product
    return product_max


def diag_down_left(list_of_rows):
    product = 1
    product_max = 1
    for i in range(17):
        for j in range(3, 20):
            product = list_of_rows[i][j]
            product *= list_of_rows[i + 1][j - 1]
            product *= list_of_rows[i + 2][j - 2]
            product *= list_of_rows[i + 3][j - 3]
            if product > product_max:
                product_max = product
    return product_max

def up(list_of_rows):
    product = 1
    product_max = 1
    for i in range(17):
        for j in range(20):
            product = list_of_rows[i][j]
            product *= list_of_rows[i + 1][j]
            product *= list_of_rows[i + 2][j]
            product *= list_of_rows[i + 3][j]
            if product > product_max:
                product_max = product
    return product_max


def right(list_of_rows):
    product = 1
    product_max = 1
    for i in range(20):
        for j in range(17):
            product = list_of_rows[i][j]
            product *= list_of_rows[i][j + 1]
            product *= list_of_rows[i][j + 2]
            product *= list_of_rows[i][j + 3]
            if product > product_max:
                product_max = product
    return product_max


product_ddr = diag_down_right(list_of_lines)
product_ddl = diag_down_left(list_of_lines)
product_up = up(list_of_lines)
product_right = right(list_of_lines)

print(product_ddl, product_ddr, product_up, product_right)

