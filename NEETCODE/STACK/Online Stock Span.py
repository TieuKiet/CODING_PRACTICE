class StockSpanner:

    def __init__(self):
        # Stack lưu dạng tuple: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        
        # Nhảy cóc: Cộng dồn span của các ngày nhỏ hơn hoặc bằng price hiện tại
        while self.stack and price >= self.stack[-1][0]:
            prev_price, prev_span = self.stack.pop()
            span += prev_span
        
        # Lưu lại (price_mới, tổng_span_đã_gộp)
        self.stack.append((price, span))
        
        return span