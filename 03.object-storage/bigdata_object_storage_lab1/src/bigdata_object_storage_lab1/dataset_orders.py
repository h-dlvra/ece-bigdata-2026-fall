import argparse
import random
from faker import Faker
from .serialize import serialize

fake = Faker()
Faker.seed(42)
random.seed(42)

PRODUCTS = ["cookie", "muffin", "coffee", "tea", "sandwich"]

def orders_generate(count_users=50, count_min=1, count_max=5, date_from="-1y", output=""):
    orders = []
    # Generates user UUIDs matching the seed used in dataset_users.py
    user_uuids = [fake.uuid4() for _ in range(count_users)]
    
    for u_uuid in user_uuids:
        num_orders = random.randint(count_min, count_max)
        for _ in range(num_orders):
            orders.append({
                "uuid": fake.uuid4(),
                "user_uuid": u_uuid,
                "date": fake.date_time_between(start_date=date_from).isoformat(),
                "quantity": random.randint(1, 5),
                "product": random.choice(PRODUCTS)
            })
    serialize(orders, output)
    return orders

def main():
    parser = argparse.ArgumentParser(prog="dataset-orders", description="Orders generator")
    parser.add_argument("-u", "--count-users", type=int, default=50, help="Number of users to generate orders for.")
    parser.add_argument("-C", "--count-min", type=int, default=1, help="Min orders per user.")
    parser.add_argument("-c", "--count-max", type=int, default=5, help="Max orders per user.")
    parser.add_argument("-d", "--date-from", default="-1y", help="Start date for orders.")
    parser.add_argument("-o", "--output", default="json", choices=["csv", "json", "jsonline"], help="Output format.")
    
    args = parser.parse_args()
    orders_generate(args.count_users, args.count_min, args.count_max, args.date_from, args.output)

if __name__ == "__main__":
    main()