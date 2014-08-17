<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/html">
<head>
    <title></title>

    <script type="text/javascript" src="js/caman.full.js" ></script>

</head>
<body>

    <script>
        Caman("#my-image", function () {
            // We can call any filter before the layer
            this.brightness(5).render();
        });
    </script>
    <img
        id="my-image"
        data-caman-hidpi="C:\Users\Samuel\Desktop\collider_project\test\files\2.jpg"
        src="imgs\2.jpg"
        style="width: 600px;"
    >
</body>
</html>