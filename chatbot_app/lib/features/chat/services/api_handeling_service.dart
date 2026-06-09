import 'dart:convert';

import 'package:chatbot_app/core/constants/urls.dart';
import 'package:chatbot_app/features/chat/models/bot_response.dart';
import 'package:http/http.dart' as http;

class APIHandlingService {
  Future<BotResponse> chat(String msg) async {
    final response = await http.post(
      Uri.parse(kChatUrl),
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: jsonEncode({ "message": msg,})
    );

    if (response.statusCode == 200) {
      final json =  jsonDecode(response.body);
      return BotResponse.fromJson(json);
    } else {
      throw Exception("Failed to chat: ${response.body}");
    }
  }
}
