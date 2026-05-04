from django import forms
from django.conf import settings
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=254,
        required=True,
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
    )
    subject = forms.CharField(
        max_length=254,
        required=True,
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True,
    )

    def send_mail(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            email = self.cleaned_data['email']
            subject = self.cleaned_data['subject']
            message = self.cleaned_data['message']

            html_content = f"""
            <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-width: 600px; margin: 0 auto;">
                <div style="background: linear-gradient(135deg, #6366f1, #8b5cf6); padding: 24px; border-radius: 12px 12px 0 0;">
                    <h2 style="color: #fff; margin: 0; font-size: 20px;">New Contact Message</h2>
                    <p style="color: rgba(255,255,255,0.8); margin: 8px 0 0; font-size: 14px;">softdevcan.com</p>
                </div>
                <div style="background: #ffffff; padding: 24px; border: 1px solid #e5e7eb; border-top: none;">
                    <table style="width: 100%; border-collapse: collapse;">
                        <tr>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; color: #6b7280; font-size: 13px; width: 80px; vertical-align: top;">From</td>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; font-size: 14px; font-weight: 600;">{name}</td>
                        </tr>
                        <tr>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; color: #6b7280; font-size: 13px; vertical-align: top;">Email</td>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; font-size: 14px;"><a href="mailto:{email}" style="color: #6366f1; text-decoration: none;">{email}</a></td>
                        </tr>
                        <tr>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; color: #6b7280; font-size: 13px; vertical-align: top;">Subject</td>
                            <td style="padding: 12px 0; border-bottom: 1px solid #f3f4f6; font-size: 14px; font-weight: 600;">{subject}</td>
                        </tr>
                    </table>
                    <div style="margin-top: 20px; padding: 16px; background: #f9fafb; border-radius: 8px; border-left: 3px solid #6366f1;">
                        <p style="color: #6b7280; font-size: 12px; margin: 0 0 8px; text-transform: uppercase; letter-spacing: 0.5px;">Message</p>
                        <p style="color: #1f2937; font-size: 14px; line-height: 1.6; margin: 0; white-space: pre-wrap;">{message}</p>
                    </div>
                </div>
                <div style="padding: 16px; text-align: center; border-radius: 0 0 12px 12px; background: #f9fafb; border: 1px solid #e5e7eb; border-top: none;">
                    <p style="color: #9ca3af; font-size: 12px; margin: 0;">You can reply directly to this email to respond to {name}.</p>
                </div>
            </div>
            """

            mail = EmailMessage(
                f"[Contact] {subject}",
                html_content,
                to=[settings.EMAIL_HOST_USER],
                reply_to=[email],
            )
            mail.content_subtype = "html"
            mail.send()
