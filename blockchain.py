genesis_block = {
	'previous_hash': '',
	'index': 0,
	'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Ariandy'

def hash_block(block):
	return 'regulus'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
	if len(blockchain) < 1:
		return None
	return blockchain[-1]

def add_transaction(recipient, sender=owner, amount=1.0):
	transaction = {
		'sender': sender,
		'recipient': recipient,
		'amount': amount
	}
	open_transactions.append(transaction)

def mine_block():
	hashed_block = hash_block(get_last_blockchain_value())
	print(hashed_block)
	block = {
		'previous_hash': hashed_block,
		'index': len(blockchain),
		'transactions': open_transactions
	}
	blockchain.append(block)

def get_transaction_value():
	tx_recipient = input('Enter the recipient of the transaction: ')
	tx_amount = float(input('Transaction amount: '))
	return tx_recipient, tx_amount

def get_user_choice():
	return input('Your choice : ')

def print_blockchain_elements():
	for block in blockchain:
		print('outputting block')
		print(block)

def verify_chain():
	for (index, block) in enumerate(blockchain):
		if index == 0:
			continue
		if block['previous_hash'] != hash_block(blockchain[index - 1]):
			return False
	return True

waiting_for_input = True

while waiting_for_input:
	print('What do you want')
	print('1: Add new transaction value')
	print('2: Mine new block')
	print('3: Output the blockchain blocks')
	print('4: Chain Manipulation')
	print('q: Quit')
	user_choice = get_user_choice()
	if user_choice == '1':
		tx_data = get_transaction_value()
		recipient, amount = tx_data
		add_transaction(recipient, amount=amount)
		print(open_transactions)
	elif user_choice == '2':
		mine_block()
	elif user_choice == '3':
		print_blockchain_elements()
	elif user_choice == 'h':
		if len(blockchain) >= 1:
			blockchain[0] = {
				'previous_hash': 'haxxor',
				'index': 333,
				'transactions': [{
					'sender': 'abigail',
					'recipient': 'gargoyle',
					'amount': 6969
				}]
			}
	elif user_choice == 'q':
		waiting_for_input = False
	else:
		print('Invalid')
	if not verify_chain():
		print_blockchain_elements()
		print('Invalid Blockchain')
		break
else:
	print('User Left')

print('Done!')