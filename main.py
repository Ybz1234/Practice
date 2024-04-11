def multiply_all_element(x):
    multiply = 1
    for number in x:
        multiply *= number
    return multiply


def get_min_and_max(x):
    return min(x), max(x)


def line_per_name(family):
    for name in family:
        print(name)


def is_family_member(family, name):
    return name in family


def full_email(email):
    return "@".join(email)


def is_ip_valid(address):
    octets = address.split(".")
    for octet in octets:
        if not 0 <= int(octet) <= 255:
            return False
    return True


def mystery(list_of_words):
    new_list = []
    for index in range(1, len(list_of_words) + 1):
        new_list.append(" ".join(list_of_words[:index]))
    return new_list


def digits_and_letters_counter(input_str):
    letters = sum(1 for char in input_str if char.isalpha())
    digits = sum(1 for char in input_str if char.isdigit())
    return letters, digits


def remove_char_at_index(text, index):
    return text[:index] + text[index + 1:]


def insert_char_at_index(text, char, index):
    return text[:index] + char + text[index:]


def replace_char_at_index(text, char, index):
    return text[:index] + char + text[index + 1:]


def only_even_indexes_str(text):
    res = ""
    for index, char in enumerate(text):
        if index % 2 == 0:
            res += char
    return res


def markup_generator(tag, text):
    return f"<{tag}>{text}<{tag}/>"


def last_2_chars_4_times(text):
    return 4 * text[-2:]


def first_3_chars(text):
    return text[:3] if 3 <= len(text) else text


def remove_duplicates(text):
    unique = ""
    for char in text:
        if char not in unique:
            unique += char
    return unique


def word_counter(text):
    return len(text.split(" "))


def get_first_and_last_words(text):
    words = text.split(" ")
    return f"{words[0]} {words[-1]}"


def reverse_string(text):
    words = text.split(" ")
    reversed_words = words[::-1]
    reversed_text = " ".join(reversed_words)
    return reversed_text


def get_middle_char(text):
    if len(text) % 2 == 0:
        return text[len(text) // 2 - 1:len(text) // 2 + 1]
    return text[len(text) // 2]


def is_reversed(text1, text2):
    temp = text2
    for letter in text1:
        if letter != temp[-1]:
            return False
        else:
            temp = temp[:-1]
    return True


def reverse(text):
    res = ""
    for letter in text:
        res += text[-1]
        text = text[:-1]
    return res


def capitalize_every_word(text):
    return text.title()


def no_punctuation(text):
    result = ""
    for char in text:
        if char.isalpha() or char.isdigit() or char.isspace():
            result += char
    return result


def is_palindrome(text):
    for i in range(len(text)):
        if text[i] != text[-i - 1]:
            return False
    return True


def array_sum(nums):
    sum = 0
    skip_next = False
    for i in range(len(nums)):
        if skip_next:
            skip_next = False
            continue
        if nums[i] != 13:
            sum += nums[i]
        else:
            skip_next = True
    return sum


def sum67(nums):
    sum = 0
    skip = False
    for num in nums:
        if num == 6:
            skip = True
            continue
        elif num == 7 and skip:
            skip = False
            continue
        elif not skip:
            sum += num
    return sum


def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False


def big_diff(nums):
    return abs(max(nums) - min(nums))


def centered_average(nums):
    sum, min_counter, max_counter = 0, 0, 0
    min_val = min(nums)
    max_val = max(nums)
    for i in range(len(nums)):
        if min_counter == 0 and nums[i] == min_val:
            min_counter += 1
            continue
        if max_counter == 0 and nums[i] == max_val:
            max_counter += 1
            continue
        else:
            sum += nums[i]
    return sum // i


def count_evens(nums):
    evens = 0
    for n in nums:
        if n % 2 == 0:
            evens += 1
    return evens


def hello_name(name):
    return f"Hello {name}"


def make_abba(a, b):
    return a + b + b + a


def make_out_word(out, word):
    return out[0] + out[1] + word + out[2] + out[3]


def double_char(text):
    return ''.join([char * 2 for char in text])


def count_hi(text):
    count = 0
    for i in range(len(text) - 1):
        if text[i:i + 2] == "hi":
            count += 1
    return count


def cat_dog(str):
    cat, dog = 0, 0
    for i in range(len(str) - 1):
        if str[i:i + 3] == "cat":
            cat += 1
        elif str[i:i + 3] == "dog":
            dog += 1
    return cat == dog


def count_code(str):
    count = 0
    for i in range(len(str) - 1):
        if str[i:i + 1] == "co" and str[i + 3] == "e":
            count += 1
    return count


def make_bricks(small, big, goal):
    max_big_needed = goal // 5
    if big >= max_big_needed:
        goal -= max_big_needed * 5
    else:
        goal -= big * 5

    return goal <= small


def main():
    print(count_hi("Hi everyone, hi ya'll."))


if __name__ == '__main__':
    main()
