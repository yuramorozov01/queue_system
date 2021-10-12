from collections import Counter

from queue_system import QueueSystem 
from graph import state_names

def calc_states_probs(states):
	str_states = list(map(lambda item: ''.join(str(value) for value in item), states))
	states_amount = Counter(str_states)
	states_probs = []
	for state, amount in states_amount.items():
		states_probs.append((state_names[state], state, amount / len(states)))
		
	states_probs.sort(key=lambda x: x[0])
	for state_number, state, prob in states_probs:
		print('P{} = {} = {:.4f}'.format(state_number, state, prob))
	return states_probs

def calc_prob_of_reject(requests):
	amount_of_rejects = 0
	for request in requests:
		if request.is_rejected:
			amount_of_rejects += 1
	return amount_of_rejects / len(requests) / 2

def calc_prob_of_block(states, requests):
	return 0

def calc_average_queue_length(states):
	sum_len = 0
	for state in states:
		sum_len += state[1]
	return sum_len / len(states)

def calc_average_requests_system(states):
	sum_len = 0
	for state in states:
		sum_len += state[1] + state[2] + state[3]
	return sum_len / len(states)

def calc_average_time_in_queue(requests):
	times = 0
	requests_without_reject = list(filter(lambda request: not request.is_rejected, requests))
	for request in requests_without_reject:
		times += request.tacts_in_queue
	return times / len(requests_without_reject)

def calc_average_time_in_system(requests):
	# requests_without_reject = list(filter(lambda request: not request.is_rejected, requests))
	times = 0
	for request in requests:
		times += request.tacts
	return times / len(requests)

def calc_measures_of_efficiency(states, requests):
	states_probs = calc_states_probs(states)
	P_reject = calc_prob_of_reject(requests)
	P_block = calc_prob_of_block(states, requests)
	Q = 1 - P_reject
	A = 0.5 * Q
	L_queue = calc_average_queue_length(states)
	L_sys = calc_average_requests_system(states)
	W_queue = calc_average_time_in_queue(requests)
	W_sys = calc_average_time_in_system(requests)

	print('P reject = {}'.format(P_reject))
	print('P block = {}'.format(P_block))
	print('Q = {}'.format(Q))
	print('A = {}'.format(A))
	print('L queue = {}'.format(L_queue))
	print('L system = {}'.format(L_sys))
	print('W queue = {}'.format(W_queue))
	print('W system = {}'.format(W_sys))

def main():
	queue_system = QueueSystem(0.7, 0.8)
	queue_system.start(200000)
	states = queue_system.history_states
	requests = queue_system.history_requests
	calc_measures_of_efficiency(states, requests)

if __name__ == '__main__':
	main()








