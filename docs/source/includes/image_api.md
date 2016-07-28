# Images

## Get All Images

```shell
curl -X GET "http://aswachhbharat.org/api/images/"
```

> The above command returns JSON structured like this:

```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [{
    "file": "http://aswachhbharat.org/media/images/2016/07/28/image_45917.png",
    "location": {
      "type": "Point",
      "coordinates": [
        15.205078, -9.316406
      ]
    }
  }, {
    "file": "http://aswachhbharat.org/media/images/2016/07/28/image_45tgf.png",
    "location": {
      "type": "Point",
      "coordinates": [
        16.611328,
        8.525391
      ]
    }
  }, {
    "file": "http://aswachhbharat.org/media/images/2016/07/28/image_5rdr5.png",
    "location": null
  }]
}
```

This endpoint retrieves all images.

### HTTP Request

`GET http://aswachhbharat.org/api/images/`


## Get a Specific Image

```shell
curl -X GET "http://aswachhbharat.org/api/images/1/"
```

> The above command returns JSON structured like this:

```json
{
  "file": "http://aswachhbharat.org/media/images/2016/07/28/image_45917.png",
  "location": {
    "type": "Point",
    "coordinates": [
      15.205078, -9.316406
    ]
  }
}
```

This endpoint retrieves a specific image.

### HTTP Request

`GET http://aswachhbharat.org/api/images/<image_id>/`

### URL Parameters

Parameter | Description | Required | Type
--------- | ----------- |--------- | ------
ID | The ID of the image to retrieve | yes | path

## Post an Image

```shell
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@[object Object]" -F "location=POINT(12.9085608 77.6106535)" "http://aswachhbharat.org/api/images/"
```

> The above command returns JSON structured like this:

```json
{
  "file": "http://aswachhbharat.org/media/images/2016/07/28/image_45917.png",
  "location": {
    "type": "Point",
    "coordinates": [
      12.9085608, 77.6106535
    ]
  }
}
```

Use this API to upload an image. Make sure you do `multipart/form-data` POST. The `location` field is a string, should be of format: `POINT(12.9085608 77.6106535)`.

### HTTP Request

`POST http://aswachhbharat.org/api/images/`

### URL Parameters

Parameter | Description | Required | Type | Data type
--------- | ----------- |--------- | ---- | ---------
file | Image file to upload | yes | form (multipart/form-data) | -
location | location of the image | no | form | String of format `POINT(12.9085608 77.6106535)`
