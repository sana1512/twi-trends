var li_elements = document.querySelectorAll(".wrapper_left ul li");
var item_elements = document.querySelectorAll(".item");

for (var i = 0; i < li_elements.length; i++) {
  li_elements[i].addEventListener("click", function() {
    
    li_elements.forEach(function(li) {
      li.classList.remove("active");
    });
    this.classList.add("active");

    var li_value = this.getAttribute("data-li");
    item_elements.forEach(function(item) {
      item.style.display = "none";
    });
    
    if (li_value == "a") {            
      document.querySelector("." + li_value).style.display = "block";                  
    } else if (li_value == "b") {            
      document.querySelector("." + li_value).style.display = "block";      
    } else if (li_value == "c") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "d") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "e") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "f") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "g") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "h") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "i") {
      document.querySelector("." + li_value).style.display = "block";
    } else if (li_value == "j") {
      document.querySelector("." + li_value).style.display = "block";
    } else {
      console.log("");
    }
    
  });
}
