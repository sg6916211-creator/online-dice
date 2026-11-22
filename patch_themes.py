import re

html = open("index.html", encoding="utf-8").read()

start = html.index('$("#theme-select").on("change"')
end = html.index('setCookie("theme",theme,365);', start) + len('setCookie("theme",theme,365);')
end = html.index('});', end) + len('});')

new_block = '''		var THEME_STYLES = {
			"blue": {a:"#08f", d:"#002f59"}, "sab-blue": {a:"#08f", d:"#002f59"},
			"green": {a:"#008000", d:"#003d00"}, "sab-green": {a:"#008000", d:"#003d00"},
			"red": {a:"#B22222", d:"#4a0000"}, "sab-red": {a:"#B22222", d:"#4a0000"},
			"pink": {a:"#EE82EE", d:"#4a004a"}, "bw": {a:"#444", d:"#111"}, "sab-black": {a:"#222", d:"#000"},
			"sab-heaven": {a:"#4aa8d8", d:"#1a3a55"}, "sab-hell": {a:"#8B0000", d:"#2a0000"},
			"sab-underwater": {a:"#006994", d:"#001a2a"}, "bronze": {a:"#a56c43", d:"#3a2400"},
			"silver": {a:"#777", d:"#222"}, "gold": {a:"#c6a44d", d:"#4a3800"}
		};

		function applyTheme(theme) {
			var t = THEME_STYLES[theme] || THEME_STYLES["sab-blue"];
			var img = "images/theme-" + theme + ".png";
			var css = "body{background:" + t.a + " url('" + img + "') no-repeat fixed center / cover !important;}" +
				"#content{background-image:none !important;}" +
				".loader{background:" + t.a + " url('" + img + "') no-repeat fixed center / cover !important;}" +
				"#footer{background:" + t.d + " !important;}" +
				".filled{background:" + t.a + " !important;}" +
				"#dice-roll-box{background:" + t.a + " !important;}" +
				".rounded-dice{background:" + t.a + " !important;}" +
				"#num-select,#type-select,select{border-color:" + t.a + " !important;color:" + t.a + " !important;}";
			var st = document.getElementById('theme-style');
			if (!st) { st = document.createElement('style'); st.id = 'theme-style'; document.head.appendChild(st); }
			st.textContent = css;
			$("meta[name=theme-color]").attr("content", t.a);
			$("meta[name=msapplication-TileColor]").attr("content", t.a);
			$("link[rel=mask-icon]").attr("color", t.a);
			setCookie("theme", theme, 365);
		}

		$("#theme-select").on("change", function() {
			applyTheme($("#theme-select").val());
		});

		function getCookie(name) {
			var m = document.cookie.match(new RegExp('(?:^|; )' + name + '=([^;]*)'));
			return m ? decodeURIComponent(m[1]) : null;
		}

		var savedTheme = getCookie("theme");
		if (savedTheme && THEME_STYLES[savedTheme]) {
			$("#theme-select").val(savedTheme);
			applyTheme(savedTheme);
		}'''

html = html[:start] + new_block + html[end:]
open("index.html", "w", encoding="utf-8").write(html)
print("theme-select JS replaced OK")
