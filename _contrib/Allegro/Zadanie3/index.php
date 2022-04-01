<?php
    require_once 'lib/ItemList.class.php';
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <style>
        li { margin-top: 4em; }
        img { max-width: 80px; max-height: 80px; }
        table { width: 90%; margin: 5em auto; border: 1px solid #000; padding: 1em}
        tr:nth-child(2n + 1) { background-color: #f7f7f7; }
        td { vertical-align: middle; text-align: center; }
        th { vertical-align: middle; text-align: left; padding-left: 2em; }
        td, th { height: 5em; }
    </style>
</head>
<body>
<form method="GET" action="#">
<select name="id">

<?php
    $categories = array(
        'apple notebooks' => '77915',
        'iphone 4' => '85852',
        'iphone 3GS' => '54003',
        'iphone 3G' => '66373',
        'iphone 2G' => '54002',
        'ipad' => '89254',
    );
    
    foreach($categories as $name => $value)
        echo '<option value="'.$value.'" value> '.$name.'</option>';
?>
</select>
<input type="submit" value="GO" />
</form>
<hr />

<?php
    $id = empty($_GET['id']) ? false : $_GET['id'];

    if ($id) {
        $link = 'http://allegro.pl/rss.php?feed=cat&id=';
        $uri = $link.$id;
    
        $content = file_get_contents($uri);  
        $feed = new SimpleXmlElement($content);
        $list = new ItemList($feed->channel->item);
        
      
        echo '<h1>'.$feed->channel->title.'</h1>';
        echo '<table>';
        
        /*
         * I know that echo is faster than either printf
         * or print itself, however this is more readable,
         * and this task does not require me to consider
         * optimization therefore I am using printf function
         */
        foreach ($list as $item) {
            printf('<tr><td class="img"><img src="%s" alt="%s" /></td><th class="title"><a href="%s">%s</a></th><td class="login">%s</td><td class="price">%s</td></tr>',
                $item->getThumbnailUrl(),
                $item->getName(),
                $item->getUri(),
                $item->getName(),
                $item->getSeller(),
                $item->getPrice()
            );
        }
        
        echo '</table>';
        echo 'showing '. $list->getCount().' items from: <a href="'.$uri.'">'.$uri.'</a>';
    }
?>


</body>
</html>