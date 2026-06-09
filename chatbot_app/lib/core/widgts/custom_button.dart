import 'package:flutter/material.dart';

Widget customButton({
  required String title,
  required Color bgColor,
  required Color textColor,
  VoidCallback? onPressed,
  double fontSize = 20
}) {
  return Material(
    color: Colors.transparent,
    child: InkWell(
      borderRadius: BorderRadius.circular(10),
      onTap: () => onPressed,
      child: Container(
        width: 150,
        height: 50,
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(10),
          color: bgColor,
        ),
        child: Center(
          child: Text(
            title,
            style: TextStyle(
              color: textColor,
              fontWeight: FontWeight.w400,
              fontSize: fontSize,
            ),
          ),
        ),
      ),
    ),
  );
}
