# Change all URLs in database
``` sql
-- basic changes
UPDATE wp_options SET option_value = replace(option_value, 'oldurl.com', 'newurl.com') WHERE option_name = 'home' OR option_name = 'siteurl';
UPDATE wp_postmeta SET meta_value = replace(meta_value,'oldurl.com','newurl.com');
UPDATE wp_usermeta SET meta_value = replace(meta_value, 'oldurl.com','newurl.com');
UPDATE wp_links SET link_url = replace(link_url, 'oldurl.com','newurl.com');
UPDATE wp_comments SET comment_content = replace(comment_content , 'oldurl.com','newurl.com');

-- images inside posts
UPDATE wp_posts SET post_content = replace(post_content, 'oldurl.com', 'newurl.com');

-- images linked in old links manager
UPDATE wp_links SET link_image = replace(link_image, 'oldurl.com','newurl.com');

-- attachments
UPDATE wp_posts SET guid = replace(guid, 'oldurl.com','newurl.com');
```  
