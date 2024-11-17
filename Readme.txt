The products (all fields and images) and categories which exists in an old (custom made) webshop, need to be imported into a PrestaShop webshop.
The webshop is selling vinyl records where the labels are organised by genre, artist, record name, release date,...
The data of the old webshop is stored in a MySQL database and files (images of the products) are stored in a folder.
We can give you phpmyadmin access to the database and ftp access for the image files.

The credentials for the new prestashop webshop:
https://jbswartshop.nl/admin062hlu25dphgmgvc3ur/
username: site@vkd.nl
password: P5feWZx&xyUNHw$

The credentials for the old webshop:
https://www.jbswart.nl/admin
username: JBSwart
Password: jbsadmin1108

MySQL: https://phpmyadmin.vkd.nl
New Prestashop webshop: username: dbujbswartshop, password: e3~98yfM2
Old webshop: username: dbujbswart, password: Y8p01am&

FTP: ftp.jbswart.nl / ftp.jbswartshop.nl (77.243.228.84)
New Prestashop webshop: username: jbswartshop-joshua, password: 5$z67uQ6d
Old webshop: username: jbswart-joshua, password: 5$z67uQ6d

Note: This webshop is currently still in use, so use it only in readonly mode and do not change anything on the old website


i think it is less complex as you initially thought it would be

For importing please use the offiical PrestaShop method with the CSV files
Don't access the Prestashop SQL database directly.

So the job is to create two CSV files (categories and products)
The actual; import into Prestashop is straight forward

If you want to test the import, then you do an import test with a small number of categories / products

Please inform me the moment you want to test a CSV file import.
Because then i can create a backup of the files/database before the import
So when the import when not successfull then we easily go back

But just first create the two csv files for categories and Products.
The actual import can be done at the end because i do not expect much issues with that.

Images are stored in img folder, for example img/p/ contains product images. And in database there are image id's.
When you upload/import image it gets new id for example 256 and then Prestashop creates images for all types defined in
Back Office > Preferences > Images, and those images are stored in img/p/2/5/6/ folder , for example img/p/2/5/6/256-home_default.jpg.

So via google you can find how to import the images and reference to these images in the products CSV file.



In prestashop, multiple images can be attached to a product
in old webshop, Because they are in "httpdocs\plaatjes\<foldername_from_table>\<image_filename_from_table>"
They suggest to put the images not in the standard "img" folder, but create a new folder in the root of Prestashop (e.g. call it "imgimport").
Then you can much easier reference the path to the image file name in the CSV file.
http://www.jbswartshop.nl/imgimport/HENNY WEYMANS  NU EN VOOR ALTIJD.jpg

The old webshop has also a Artist field in the products table
The new webshop does not have this field.
But i think we should create a category called "Artiest" (which is dutch for "Artist"
And we should create for each artist a subcategory
The products should be linked to the sub-category of the artist
By doing so, webshop customer can filter on artist

Regarding the article no: you can store this in the "Reference #" field

I think that the price in the old webshop is including 21% VAT
And i believe that the price in the new webshop should be excluding VAT
So price in Prestashop should be : <oldprice> / 1.21

The "onsale"is not important and i think that this should be set to 0
They can later put articles "on sale" manually

"aantal". This is the stock level quantity

"prijs" is the actual product price
The values in "oudeprijs" (old price) can be ignored

Regarding the product "Name" in prestashop
I think that we should combine two fields here (tile & artist) separated by a " | "
"name" = "<artiest> | title"

So e.g. name = "Sylvia | Ik vond bij jou het geluk"

The field "aanbieding" can be ignored
The field "xtra" and "xtraName" can be ignored

It think that the field "omschrijving" and "tracklist" should be combined in the "desciption" field
Both are text fields
It might be that we should remove html tags and , because otherwise it shows html tags and things like "&nbsp;"
The field "release datum" can be appended to the description field.
So description field is a combination of "omschrijving" + "tracklist" and "releasedatum"

So:
<omschrijving>
<tracklist>
Release datum: <day(ReleaseDatum)>><month(ReleaseDatum)><year(ReleaseDatum)>

The field "pakketverzending" has to do if the product can be shipped as a letter (maximum 3,5cm thick package), or that it has to be shipped a real package (more expensive)
We could use the field "weight" for that
So
when "pakketverzending" = 0, then weight =0
when "pakketverzending" <> 0, then weight = 2kg

Package with a weight of more than 2kg, are always normal packages.

https://www.prestashop.com/forums/topic/35408-solved-csv-import-images/