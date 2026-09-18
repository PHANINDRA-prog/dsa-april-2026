items = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)

        total_value = 0.0

        # 2. Run your corrected loop over the sorted items
        for v, w in items:
            if w <= capacity:
                total_value += v
                capacity -= w
            else:
                fraction = capacity / w
                total_value += round(fraction * v, 6)
                break  # Capacity is hit, stop processing

        return total_value