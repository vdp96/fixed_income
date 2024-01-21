import pandas as pd
import numpy as np


def bond_price(coupon_rate: float, ytm: float, t: float, face_value: float, n_coupons: int) -> float:
    annuity = face_value * ((coupon_rate / n_coupons) / (ytm / n_coupons)) * (
            1 - 1 / (1 + ytm / n_coupons) ** (n_coupons * t))

    price = annuity + face_value / (1 + ytm / n_coupons) ** (n_coupons * t)
    return price


def macaulay_duration(coupon_rate: float, ytm: float, t: int, face_value: float, n_coupons: int) -> float:
    coupon = coupon_rate / n_coupons * face_value
    n_periods = n_coupons * t
    discount_rate = ytm / n_coupons

    cash_flows = np.array([coupon] * n_periods)
    cash_flows[-1] += face_value

    times = np.array(range(1, n_periods + 1))
    pv_factors = 1 / (1 + discount_rate) ** times
    pv_cash_flows = cash_flows * pv_factors
    weighted_pv_cash_flows = pv_cash_flows * times

    duration = (weighted_pv_cash_flows.sum() / pv_cash_flows.sum()) / n_coupons
    return duration


def modified_duration(coupon_rate: float, ytm: float, t: int, face_value: float, n_coupons: int) -> float:
    mcd = macaulay_duration(coupon_rate, ytm, t, face_value, n_coupons)
    md = mcd / (1 + ytm / n_coupons)
    return md


def dv01(d_star: float, price: float) -> float:
    return d_star * price * 1e-4


def convexity(coupon_rate: float, ytm: float, t: int, face_value: float, n_coupons: int) -> float:
    coupon = coupon_rate / n_coupons * face_value
    n_periods = n_coupons * t
    discount_rate = ytm / n_coupons

    cash_flows = np.array([coupon] * n_periods)
    cash_flows[-1] += face_value

    times = np.array(range(1, n_periods + 1))
    pv_factors = 1 / (1 + discount_rate) ** times
    pv_cash_flows = cash_flows * pv_factors

    c = (np.sum(pv_cash_flows * times * (times + 1)) / np.sum(pv_cash_flows)) / n_coupons ** 2
    c /= (1 + discount_rate) ** 2
    return c


def interest_rate_NSS(b0: float, b1: float, b2: float, b3: float, tau1: float, tau2: float, t: float) -> float:
    e = np.exp

    t1 = t / tau1
    t2 = t / tau2

    rt = b0 + (b1 * (1 - e(-t1)) / t1) + (b2 * ((1 - e(-t1)) / t1 - e(-t1))) + (b3 * ((1 - e(-t2)) / t2 - e(-t2)))
    return rt
