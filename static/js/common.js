		// 首屏点击展开
		$(".nav").hover(
		function (e) {
			$(".nav-ul").slideDown();
			$(".nav-img").attr("src", "img/daohang-g.png").stop().animate({
				left: 10 + "%"
			}, 300);
			e.stopPropagation();
		}, function (e) {
			$(".nav-ul").stop().slideUp()
			$(".nav-img").attr("src", "img/daohang-k.png").stop().animate({
				left: 14 + "%"
			}, 300)
			e.stopPropagation()
		}
	);