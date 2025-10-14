class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0] *n
        call_stack = []
        prev_time = 0

        for log in logs:
            fun_id,call_type, timestamp = log.split(":")

            fun_id = int(fun_id)
            timestamp = int(timestamp)

            if call_type == "start":
                if call_stack:
                    exclusive_time[call_stack[-1]] += timestamp - prev_time
                
                call_stack.append(fun_id)
                prev_time = timestamp
            else:
                exclusive_time[call_stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return exclusive_time  

        