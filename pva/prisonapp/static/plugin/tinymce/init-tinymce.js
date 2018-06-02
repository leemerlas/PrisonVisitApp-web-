
tinymce.init({
    /* replace textarea having class .tinymce with tinymce editor */
    selector: "#mytextarea",

    /* theme of the editor */
    theme: "modern",
    skin: "lightgray",


    /* width and height of the editor */
    width: "100%",
    height: "500",

    /* display statusbar */
    statusbar: true,

    /* plugin */
    plugins: [
        "advlist print preview",
        "save contextmenu directionality emoticons paste textcolor wordcount",
        "image imagetools"
    ],

    /* toolbar */
    toolbar: "undo redo | styleselect | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | forecolor backcolor | link image",

    /* style */
    style_formats: [
        {
            title: "Headers", items: [
            {title: "Header 1", format: "h1"},
            {title: "Header 2", format: "h2"},
            {title: "Header 3", format: "h3"},
            {title: "Header 4", format: "h4"},
            {title: "Header 5", format: "h5"},
            {title: "Header 6", format: "h6"}
        ]
        },
        {
            title: "Inline", items: [
            {title: "Bold", icon: "bold", format: "bold"},
            {title: "Italic", icon: "italic", format: "italic"},
            {title: "Underline", icon: "underline", format: "underline"},
            {title: "Strikethrough", icon: "strikethrough", format: "strikethrough"},
            {title: "Superscript", icon: "superscript", format: "superscript"},
            {title: "Subscript", icon: "subscript", format: "subscript"},
            {title: "Code", icon: "code", format: "code"}
        ]
        },
        {
            title: "Blocks", items: [
            {title: "Paragraph", format: "p"},
            {title: "Blockquote", format: "blockquote"},
            {title: "Div", format: "div"},
            {title: "Pre", format: "pre"}
        ]
        },
        {
            title: "Alignment", items: [
            {title: "Left", icon: "alignleft", format: "alignleft"},
            {title: "Center", icon: "aligncenter", format: "aligncenter"},
            {title: "Right", icon: "alignright", format: "alignright"},
            {title: "Justify", icon: "alignjustify", format: "alignjustify"}
        ]
        }
    ],
    images_upload_handler: function (blobInfo, success, failure) {
        var xhr, formData;
        xhr = new XMLHttpRequest();
        xhr.withCredentials = false;
        xhr.open('POST', 'https://api.cloudinary.com/v1_1/strova/upload');

        xhr.onload = function () {
            var json;
            var select = document.getElementById('mytextarea');
            if (xhr.status !== 200) {
                failure('HTTP Error: ' + xhr.status);
                return;
            }

            json = JSON.parse(xhr.responseText);


            success(json.secure_url);
            console.log(json.secure_url);
            var imagesrc = document.createElement('img');
            imagesrc.setAttribute('src', json.secure_url);
            select.appendChild(imagesrc);

        };

        formData = new FormData();
        formData.append('file', blobInfo.blob(), blobInfo.filename());
        formData.append('upload_preset', 'z6pni3zq');

        xhr.send(formData);
    }
});
