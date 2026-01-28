#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        # =====================
    # 正常系（仕様を満たす入力）
    # =====================

    def test_normal_case(self):
        # 仕様上、a < b の制約は存在しない
        self.assertEqual(21, calc(3, 7))

    def test_order_not_required(self):
        # a >= b でも仕様上は有効
        self.assertEqual(21, calc(7, 3))


    # =====================
    # 境界値分析（有効範囲）
    # =====================

    def test_boundary_min(self):
        # 最小値境界
        self.assertEqual(1, calc(1, 1))

    def test_boundary_max(self):
        # 最大値境界
        self.assertEqual(998001, calc(999, 999))


    # =====================
    # 範囲外入力（無効）
    # =====================

    def test_lower_out_of_range(self):
        self.assertEqual(-1, calc(0, 10))

    def test_upper_out_of_range(self):
        self.assertEqual(-1, calc(1000, 10))


    # =====================
    # 同値分割：型・形式エラー
    # =====================

    def test_non_numeric_both(self):
        # 両方非数値
        self.assertEqual(-1, calc("a", "b"))

    def test_one_side_numeric(self):
        # 片方だけ数値（OR 条件の誤りを検出）
        self.assertEqual(-1, calc("3", "a"))


    # =====================
    # 整数限定仕様違反の検出
    # =====================

    def test_float_input(self):
        # float 型は仕様違反
        self.assertEqual(-1, calc(0.1, 10))

    def test_decimal_string(self):
        # 小数文字列は仕様違反（正規表現の誤りを検出）
        self.assertEqual(-1, calc("0.1", "10"))

    def test_float_string_conversion(self):
        # float() により通ってしまう問題を検出
        self.assertEqual(-1, calc("1.5", "2"))


