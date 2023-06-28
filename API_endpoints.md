`POST /boards`
{
  "owner": "John Doe",
  "title": "title",
}

Returns:
```
{
    "board": {
        "board_id": 4,
        "owner": "Enrique",
        "title": "Summer"
    }
}
```

`GET /boards`

Returns:
```
[
    {
        "board_id": 1,
        "owner": "Laura",
        "title": "vacation"
    },
    {
        "board_id": 2,
        "owner": "Cecilia",
        "title": "About cooking"
    },
    {
        "board_id": 3,
        "owner": "Andrea",
        "title": "Painting ideas"
    },
    {
        "board_id": 4,
        "owner": "Enrique",
        "title": "Summer"
    }
]
```
`POST /boards/{board-id}/cards`
{"message": "get Donuts!"}

Returns:
```
{
    "card": {
        "board_id": 4,
        "card_id": 7,
        "likes_count": null,
        "message": "Get donuts!"
    }
}
```

`GET /boards/{board-id}/cards`

Gets all the cards in a board

```
[
    {
        "board_id": 3,
        "card_id": 5,
        "likes_count": 3,
        "message": "Be positive"
    },
    {
        "board_id": 3,
        "card_id": 6,
        "likes_count": null,
        "message": "colors are life"
    }
]
```

`DELETE /cards/{card-id}`

`PUT /cards/{card-id}/like`
Returns:
```
{
    "board_id": 4,
    "card_id": 7,
    "likes_count": 1,
    "message": "Get donuts!"
}
```


