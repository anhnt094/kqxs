import argparse
import re
import requests


def find_number(id, text):
    index = text.find(id)
    return re.split('[<>]', text[index: index + 150])[1]


def get_data_from_ketqua_net():
    url = 'http://ketqua.net/'
    response = requests.get(url)

    numbers = {}

    numbers['Giải đặc biệt'] = [find_number('id="rs_0_0"', response.text)]

    numbers['Giải nhất'] = [find_number('id="rs_1_0"', response.text)]

    numbers['Giải nhì'] = [find_number('id="rs_2_0"', response.text),
                           find_number('id="rs_2_1"', response.text)]

    numbers['Giải ba'] = [find_number('id="rs_3_0"', response.text),
                          find_number('id="rs_3_1"', response.text),
                          find_number('id="rs_3_2"', response.text),
                          find_number('id="rs_3_3"', response.text),
                          find_number('id="rs_3_4"', response.text),
                          find_number('id="rs_3_5"', response.text)]

    numbers['Giải tư'] = [find_number('id="rs_4_0"', response.text),
                          find_number('id="rs_4_1"', response.text),
                          find_number('id="rs_4_2"', response.text),
                          find_number('id="rs_4_3"', response.text)]

    numbers['Giải năm'] = [find_number('id="rs_5_0"', response.text),
                           find_number('id="rs_5_1"', response.text),
                           find_number('id="rs_5_2"', response.text),
                           find_number('id="rs_5_3"', response.text),
                           find_number('id="rs_5_4"', response.text),
                           find_number('id="rs_5_5"', response.text)]

    numbers['Giải sáu'] = [find_number('id="rs_6_0"', response.text),
                           find_number('id="rs_6_1"', response.text),
                           find_number('id="rs_6_2"', response.text)]

    numbers['Giải bảy'] = [find_number('id="rs_7_0"', response.text),
                           find_number('id="rs_7_1"', response.text),
                           find_number('id="rs_7_2"', response.text),
                           find_number('id="rs_7_3"', response.text)]

    return numbers


def is_winning_number(check_number):
    result = False
    winning_number_list = get_data_from_ketqua_net()
    for giai_thuong in winning_number_list:
        for nums in winning_number_list[giai_thuong]:
            if check_number[-2:] == nums[-2:]:
                result = True
                print('Trúng lô {} - {}'.format(giai_thuong, nums))

    if not result:
        print('Không trúng lô')
    return result


def print_all_numbers():
    winning_number_list = get_data_from_ketqua_net()
    for giai_thuong in winning_number_list:
        print('{}:'.format(giai_thuong))
        for nums in winning_number_list[giai_thuong]:
            print('\t\t{}'.format(nums))


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra lô")
    parser.add_argument('number', nargs='*', help='Số cần kỉêm tra')
    args = parser.parse_args()

    numbers = args.number
    if not numbers:
        print_all_numbers()
    else:
        for num in numbers:
            is_winning_number(num)


if __name__ == '__main__':
    main()
