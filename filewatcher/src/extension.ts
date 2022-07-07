// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from 'vscode';
import { findNodeAtLocation, parseTree } from "jsonc-parser";
import { ConsoleReporter } from '@vscode/test-electron';
// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {

	const watcher: vscode.FileSystemWatcher = vscode.workspace.createFileSystemWatcher("**/*.{json}", false, false, false);
	watcher.onDidChange((uri: vscode.Uri) => {
		// IMPORTANT: Compile typescript file to javascript with STRG+SHIFT+B
		console.log("File changed : " + uri.fsPath);
		//Disable caching, else the change will not appear in output
		delete require.cache[uri.fsPath];
		var json = require(uri.fsPath);

		// var json1 = JSON.parse(json);
		var text =JSON.stringify(json);
		console.log(json);
		const rootNode = parseTree(text);
		if(rootNode !== undefined ){
			
		// 	// Find first element of the "components" array
			const firstComponent = findNodeAtLocation(rootNode, ["API"]);
			
			if(firstComponent !== undefined ){
				console.log(firstComponent);	
				if(json !== undefined ){
					console.log(firstComponent.offset);
					const start = json.positionAt(firstComponent.offset);
					const end = json.positionAt(firstComponent.offset+ firstComponent.length);
					console.log("TEST1");
					const range = new vscode.Range(start, end);
					console.log(range);
					let diagnosticCollection = vscode.languages.createDiagnosticCollection("Output");
					let diagnostics : vscode.Diagnostic[] = [];
					diagnostics.push(new vscode.Diagnostic(range, "Output", vscode.DiagnosticSeverity.Warning));
					// Ctrl+Shift+B To compile
					console.log(diagnostics);
					diagnosticCollection.set(uri, diagnostics);
				}
			}
		}


	});

}

// this method is called when your extension is deactivated
export function deactivate() {}
