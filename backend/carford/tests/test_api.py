def test_cars_get_all(client, cars):  # Arrange
    """Test get all cars"""
    # Act
    response = client.get("/api/v1/car/")
    # Assert
    assert response.status_code == 200
    data = response.json["cars"]
    assert len(data) == 3
    for car in cars:
        assert car.id in [item["id"] for item in data]
        assert car.color in [item["color"] for item in data]
        assert car.model in [item["model"] for item in data]


def test_cars_get_one(client, cars):  # Arrange
    """Test get one car"""
    for car in cars:
        # Act
        response = client.get(f"/api/v1/car/{cars.id}")
        data = response.json
        # Assert
        assert response.status_code == 200
        assert data["color"] == car.color
        assert data["model"] == car.model
        

def test_order_get_all(client, orders):  # Arrange
    """Test get all orders"""
    # Act
    response = client.get("/api/v1/order/")
    # Assert
    assert response.status_code == 200
    data = response.json["orders"]
    assert len(data) == 3
    for order in orders:
        assert order.id in [item["id"] for item in data]
        assert order.user_id in [item["user_id"] for item in data]
        assert order.car_id in [item["car_id"] for item in data]


def test_orders_get_one(client, orders):  # Arrange
    """Test get one car"""
    for order in orders:
        # Act
        response = client.get(f"/api/v1/order/{orders.id}")
        data = response.json
        # Assert
        assert response.status_code == 200
        assert data["order_id"] == order.id
