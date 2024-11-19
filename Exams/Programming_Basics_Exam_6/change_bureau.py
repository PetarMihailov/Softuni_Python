bitcoins = int(input())
yuans = float(input())
commission_percent = float(input())

bitcoin_to_bgn = 1168
yuan_to_usd = 0.15
usd_to_bgn = 1.76
bgn_to_eur = 1.95

bitcoins_to_bgn = bitcoins * bitcoin_to_bgn
yuans_to_bgn = (yuans * yuan_to_usd) * usd_to_bgn
total_bgn = bitcoins_to_bgn + yuans_to_bgn
total_eur = total_bgn / bgn_to_eur

commission = total_eur * (commission_percent / 100)
final_sum = total_eur - commission

print(f"{final_sum:.2f}")
